from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ServiceModelForm, MyDetailsModelForm, ParcelDetailsModelForm, usersBookingDataForm, returnDetailsForm, deliveryDetailsForm, deliveryGuaranteeForm
from .models import SalesData,DeliveryService, myDetailsModel, returnDetailsModel, usersBookingData, deliveryDetailsData, ServiceUserModel, ServiceModel, ServicePacketingDeliveryMainModel
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User


from decimal import Decimal

@login_required
def index(request, user_service_id=0):
    if request.method == "POST":
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            service_instance = form.save(commit=False)
            service_instance.user = request.user 
            service_instance.save()

            return redirect('services:select_service', user_service_id=0)
    else:
        form = ServiceModelForm()
    return render(request, "services/services.html", {'form': form})


# def select_service(request, user_service_id=None):
#     services = DeliveryService.objects.all()

#     if request.method == 'POST':
#         selected_service_id = request.POST.get('selected_service')
#         selected_service = DeliveryService.objects.get(id=selected_service_id)

#         user = request.user
#         user_service_instance = ServiceUserModel.objects.create(
#             user=user,
#             service_model_data=selected_service
#         )

#         return redirect('services:details_view',  main_model_id=user_service_instance.id)

#     return render(request, 'services/select_service.html', {'services': services})


def select_service(request, user_service_id=None):
    services = DeliveryService.objects.all()
    sales_data = SalesData.objects.select_related('selected_service_sale').last()

    if request.method == 'POST':
        selected_service_id = request.POST.get('selected_service')
        selected_service = DeliveryService.objects.get(id=selected_service_id)

        # Check if the sale has been applied to this service
        if not ServiceUserModel.objects.filter(user=request.user, service_model_data=selected_service, sale_applied=True).exists():
            # Calculate the price only if the sale hasn't been applied yet
            price = selected_service.price
            if sales_data and selected_service == sales_data.selected_service_sale:
                price = price - (price * sales_data.percentage_value / 100)
                selected_service.price = price
                selected_service.save()
                print(f"Discounted Price: {price}")

        # Create a new instance of ServiceUserModel
        user_service_instance = ServiceUserModel(
            user=request.user,
            service_model_data=selected_service,
            sale_applied=True
        )
        user_service_instance.save()

        return redirect('services:details_view', main_model_id=user_service_instance.id)

    sale_context = {}
    if sales_data:
        sale_context = {
            'sale_service_id': sales_data.selected_service_sale.id,
            'sales_data_percentage': sales_data.percentage_value
        }

    context = {
        'services': services,
        **sale_context
    }

    return render(request, 'services/select_service.html', context)

def details_view(request, main_model_id=None):
    service_instance = ServiceModel.objects.last()

    form1 = MyDetailsModelForm()
    form2 = ParcelDetailsModelForm()
    form3 = usersBookingDataForm()

    if request.method == "POST":
        form1 = MyDetailsModelForm(request.POST)
        form2 = ParcelDetailsModelForm(request.POST)
        form3 = usersBookingDataForm(request.POST, initial={'form1': form1, 'form2': form2})

        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            my_details_instance = form1.save(commit=False)
            my_details_instance.user = request.user  
            my_details_instance.save()

            parcel_details_instance = form2.save()
            booking_data_instance = form3.save(commit=False)
            booking_data_instance.user = request.user
            booking_data_instance.user_details_data = my_details_instance
            booking_data_instance.parcels_details_data = parcel_details_instance
            booking_data_instance.save()

            main_model_instance = get_object_or_404(ServicePacketingDeliveryMainModel, pk=main_model_id)

            return redirect('services:details_view2', main_model_id=main_model_instance.id)
        else:
            for field, errors in form1.errors.items():
                for error in errors:
                    messages.error(request, f"Form 1 Error: {error}")

            for field, errors in form2.errors.items():
                for error in errors:
                    messages.error(request, f"Form 2 Error: {error}")

            for field, errors in form3.errors.items():
                for error in errors:
                    messages.error(request, f"Form 3 Error: {error}")

            return redirect('services:details_view2', user_service_id=user_service_id)

    return render(request, "services/details_view.html", {'form1': form1, 'form2': form2, 'form3': form3})

def details_view2(request, main_model_id=None):
    user = request.user
    user_info = myDetailsModel.objects.filter(user=user).last()
    booking_data_instance = usersBookingData.objects.filter(user=user).last()
    service_user_instance = ServiceUserModel.objects.filter(user=user).last()
    service_instance = ServiceModel.objects.filter(user=user).last()

    if request.method == "POST":
        form1_addr = returnDetailsForm(request.POST)
        form2_addr = deliveryDetailsForm(request.POST)
        form3_addr = deliveryGuaranteeForm(request.POST)

        if form1_addr.is_valid() and form2_addr.is_valid() and form3_addr.is_valid():
            return_details_instance = form1_addr.save()
            delivery_details_instance = form2_addr.save()
            guarantee_details_instance = form3_addr.save()

            delivery_data_instance = deliveryDetailsData.objects.create(
                user=user,
                return_details=return_details_instance,
                delivery_details=delivery_details_instance,
                guarantee_details=guarantee_details_instance
            )

            main_model_instance = ServicePacketingDeliveryMainModel.objects.create(
                user=user,
                user_booking_data_model=booking_data_instance,
                delivery_data_model=delivery_data_instance,
                service_data_model=service_user_instance,
                serviceModelInfo=service_instance
            )

            return redirect('services:details_summary')
    else:
        # Instantiate empty forms for GET requests
        form1_addr = returnDetailsForm()
        form2_addr = deliveryDetailsForm()
        form3_addr = deliveryGuaranteeForm()

    return render(request, "services/details_view2.html", {'form1_addr': form1_addr, 'form2_addr': form2_addr, 'form3_addr': form3_addr})

def details_summary(request):
    user = request.user
    recent_service_packeting_instance = ServicePacketingDeliveryMainModel.objects.filter(user=user).order_by('-id').first()

    if recent_service_packeting_instance:
        user_booking_data = recent_service_packeting_instance.user_booking_data_model
        delivery_data = recent_service_packeting_instance.delivery_data_model
        service_data = recent_service_packeting_instance.service_data_model
        serviceModelInfo = recent_service_packeting_instance.serviceModelInfo
    else:
        user_booking_data = None
        delivery_data = None
        service_data = None
        serviceModelInfo = None

    return render(request, "services/details_summary.html", {
        'user_booking_data': user_booking_data,
        'delivery_data': delivery_data,
        'service_data': service_data,
        'serviceModelInfo': serviceModelInfo,
    })



def orderDestination(request):
    current_user = request.user
    last_service_model = ServiceModel.objects.filter(user=current_user).last()
    sender_address = deliveryDetailsData.objects.filter(user=current_user).last()
    receiver_address = deliveryDetailsData.objects.filter(user=current_user).last()

    return render(request, 'services/orderDestination.html', {
        'last_service_model': last_service_model,
        'sender_address': sender_address,
        'receiver_address': receiver_address,
    })


def successful_order(request):
    user = request.user
    recent_service_packeting_instance = ServicePacketingDeliveryMainModel.objects.filter(user=user).order_by('-id').first()
    admin_user = User.objects.filter(is_staff=True, is_superuser=True).first()
    admin_email = admin_user.email

    if recent_service_packeting_instance:
        user_booking_data = recent_service_packeting_instance.user_booking_data_model
        delivery_data = recent_service_packeting_instance.delivery_data_model
        service_data = recent_service_packeting_instance.service_data_model
        serviceModelInfo = recent_service_packeting_instance.serviceModelInfo
    else:
        user_booking_data = None
        delivery_data = None
        service_data = None
        serviceModelInfo = None

    user_details = myDetailsModel.objects.filter(user=user).order_by('-id').first()
    recipient_email = user_details.email

    # Email for the client
    subject = 'Your service is booked!'
    message = render_to_string('services/success_email.txt', {
        'user_booking_data': user_booking_data,
        'delivery_data': delivery_data,
        'service_data': service_data,
        'serviceModelInfo': serviceModelInfo,
        'user': user,
    })
    send_mail(subject, message, 'enisg1489@gmail.com', [recipient_email])

    # Email for the admin
    subject = 'A user just booked a service!'
    message = render_to_string('services/success_email_admin.txt', {
        'user_booking_data': user_booking_data,
        'delivery_data': delivery_data,
        'service_data': service_data,
        'serviceModelInfo': serviceModelInfo,
        'user': user,
    })
    send_mail(subject, message, 'enisg1489@gmail.com', [admin_email])

    return render(request, "services/successful_order.html")
