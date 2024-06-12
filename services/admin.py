from django.contrib import admin


from .models import SalesData, SendToModel, SendFromModel, ServiceModel, DeliveryService, myDetailsModel,  myParcelDetailsModel, usersBookingData, UserAttrModel, returnDetailsModel, deliveryDetailsModel, deliveryGuaranteeOptions, deliveryDetailsData, ServiceUserModel, ServicePacketingDeliveryMainModel

# Register your models here.

admin.site.register(SalesData)

admin.site.register(SendToModel)
admin.site.register(SendFromModel)
admin.site.register(ServiceModel)
admin.site.register(DeliveryService)

admin.site.register(myParcelDetailsModel)
admin.site.register(myDetailsModel)
admin.site.register(usersBookingData)
admin.site.register(UserAttrModel)

admin.site.register(returnDetailsModel)
admin.site.register(deliveryDetailsModel)
admin.site.register(deliveryGuaranteeOptions)
admin.site.register(deliveryDetailsData)
admin.site.register(ServiceUserModel)
admin.site.register(ServicePacketingDeliveryMainModel)






