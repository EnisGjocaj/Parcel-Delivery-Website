from django.shortcuts import render, redirect
from services.models import DeliveryService

from . forms import SignupForm

from django.core.mail import send_mail

from services.models import myParcelDetailsModel, ServicePacketingDeliveryMainModel

# Create your views here.
def index(request):

	return render(request, "core/index.html")


from django.template.loader import render_to_string

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Send email to the user
            subject = 'Welcome to Our Site!'
            message = render_to_string('core/signup_email.txt', {'user': user})
            user_email = form.cleaned_data.get('email')
            send_mail(subject, message, 'enisg1489@gmail.com', [user_email])

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})



# def track_parcel(request):
#     if request.method == 'POST':
#         parcel_name = request.POST.get('parcel_name')
        
#         try:
#             parcel_data = ServicePacketingDeliveryMainModel.objects.get(user=request.user, user_booking_data_model__parcels_details_data__parcel_contents=parcel_name)
#             destination = f"Destination: {parcel_data.delivery_data_model.delivery_details.delivery_full_name}"
#         except ServicePacketingDeliveryMainModel.DoesNotExist:
#             destination = "Parcel not found"
#         return render(request, 'core/base.html', {'destination': destination})
#     else:
#         return render(request, 'core/base.html')