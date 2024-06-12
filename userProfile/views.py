from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.views import generic

from . forms import UserProfileForm
from . models import UserProfile

from services.models import ServicePacketingDeliveryMainModel

# Create your views here.

# @login_required
# def profile_showcase(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     user = request.user

#     recent_service_packeting_instances = ServicePacketingDeliveryMainModel.objects.filter(user=user)

#     user_services = ServicePacketingDeliveryMainModel.objects.filter(user=user)
    
#     num_services_booked = user_services.count()

#     user_booking_data = []
#     delivery_data = []
#     service_data = []
#     serviceModelInfo = []

#     for instance in recent_service_packeting_instances:
#         user_booking_data.append(instance.user_booking_data_model)
#         delivery_data.append(instance.delivery_data_model)
#         service_data.append(instance.service_data_model)

#         serviceModelInfo.append(instance.serviceModelInfo)

#     return render(request, 'userProfile/indexProfile.html', {
#         'user_profile': user_profile,
#         'user_booking_data': user_booking_data,
#         'delivery_data': delivery_data,
#         'service_data': service_data,
#         'serviceModelInfo': serviceModelInfo,
#         'user': user,
#         'num_services_booked': num_services_booked,
#     })



@login_required
def profile_showcase(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user = request.user

    recent_service_packeting_instances = ServicePacketingDeliveryMainModel.objects.filter(user=user).distinct()

    for instance in recent_service_packeting_instances:
        print(instance)
        print(instance.id) 

    num_services_booked = recent_service_packeting_instances.count()

    print("Number of services booked:", num_services_booked)  
    
    return render(request, 'userProfile/indexProfile.html', {
        'recent_service_packeting_instances': recent_service_packeting_instances,
        'num_services_booked': num_services_booked,
        'user_profile': user_profile,
    })


# @login_required
# def profile_showcase(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     user = request.user

#     # Retrieve all service packeting instances for the user
#     recent_service_packeting_instances = ServicePacketingDeliveryMainModel.objects.filter(user=user)

#     # Count the number of services booked
#     num_services_booked = recent_service_packeting_instances.count()

#     return render(request, 'userProfile/indexProfile.html', {
#         'user_profile': user_profile,
#         'recent_service_packeting_instances': recent_service_packeting_instances,
#         'num_services_booked': num_services_booked,
#     })


# @login_required
# def profile_showcase(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)

#     user = request.user

#     recent_service_packeting_instance = ServicePacketingDeliveryMainModel.objects.filter(user=user)

#     print(recent_service_packeting_instance)


#     if recent_service_packeting_instance:

#         user_booking_data = recent_service_packeting_instance.user_booking_data_model
#         delivery_data = recent_service_packeting_instance.delivery_data_model
#         service_data = recent_service_packeting_instance.service_data_model
#         serviceModelInfo = recent_service_packeting_instance.serviceModelInfo
#     else:
#         user_booking_data = None
#         delivery_data = None
#         service_data = None
#         serviceModelInfo = None
    

#     print(user_booking_data)


#     return render(request, 'userProfile/indexProfile.html', {
#         'user_profile': user_profile,
#         'user_booking_data': user_booking_data,
#         'delivery_data': delivery_data,
#         'service_data': service_data,
#         'serviceModelInfo': serviceModelInfo,
#         'user': user,
#     })

@login_required
def profile_modify(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('userProfile:profile_showcase')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'userProfile/profile_modify.html', {
        'form': form, 
    })
