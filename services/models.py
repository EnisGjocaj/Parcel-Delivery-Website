from django.db import models

from django.contrib.auth.models import User

from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class SendFromModel(models.Model):
    name = models.CharField(max_length=100, default="UnknownW")

    def __str__(self):
        return self.name


class SendToModel(models.Model):
    name = models.CharField(max_length=100, default="UnknownW")
    sendFrom = models.ForeignKey(SendFromModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    


class ServiceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=124, default="Unknown", null=True, blank=True)
    sendFrom = models.ForeignKey("SendFromModel", on_delete=models.SET_NULL, blank=True, null=True)
    sendTo = models.ForeignKey("SendToModel", on_delete=models.SET_NULL, blank=True, null=True)
    weight = models.IntegerField(null=True, blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.name} - {self.sendFrom} - {self.sendTo}"


class UserAttrModel(models.Model):
    user_attr = models.CharField(max_length=25)

    def __str__(self):
        return self.user_attr


class DeliveryService(models.Model):
    SPEED_UNIT_CHOICES = [
        ('hours', 'Hours'),
        ('days', 'Days'),
    ]
    
    name = models.CharField(max_length=250)
    speed = models.DecimalField(max_digits=10, decimal_places=2)
    speed_unit = models.CharField(max_length=10, choices=SPEED_UNIT_CHOICES, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='delivery_service_images/', blank=True, null=True)
    # sale = models.OneToOneField(Sale, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class SalesData(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	percentage_value = models.IntegerField()
	selected_service_sale = models.ForeignKey(DeliveryService, on_delete=models.CASCADE)

# class DeliveryService(models.Model):
#     SPEED_UNIT_CHOICES = [
#         ('hours', 'Hours'),
#         ('days', 'Days'),
#     ]
    
#     name = models.CharField(max_length=250)
#     speed = models.DecimalField(max_digits=10, decimal_places=2)
#     speed_unit = models.CharField(max_length=10, choices=SPEED_UNIT_CHOICES, blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.DecimalField(max_digits=5, decimal_places=2)
#     image = models.ImageField(upload_to='delivery_service_images/', blank=True, null=True)

#     def discounted_price(self):
#         return self.price - (self.price * (self.sale_percentage / 100))

#     def __str__(self):
#         return self.name







# class Sale(models.Model):
#     service = models.OneToOneField(DeliveryService, on_delete=models.CASCADE)
#     percentage_discount = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))])

#     def apply_discounted_price(self):
#         return self.service.price - (self.service.price * (self.percentage_discount / 100))
    
#     def __str__(self):
#         return f"{self.service} - {self.percentage_discount}"


class myDetailsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_attr = models.ForeignKey(UserAttrModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class myParcelDetailsModel(models.Model):
    parcel_contents = models.CharField(max_length=255)
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()

    def __str__(self):
        return self.parcel_contents


class usersBookingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    terms_and_conditions = models.BooleanField(default=False)
    user_details_data = models.ForeignKey("myDetailsModel", on_delete=models.CASCADE, null=True)
    parcels_details_data = models.ForeignKey("myParcelDetailsModel", on_delete=models.CASCADE, null=True)
    #test field below 
    service_data_model = models.ForeignKey('ServiceUserModel', on_delete=models.CASCADE, null=True, blank=True)


class returnDetailsModel(models.Model):
    return_full_name = models.CharField(max_length=200)
    return_address = models.CharField(max_length=100)
    return_postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.return_full_name} - {self.return_address}"


class deliveryDetailsModel(models.Model):
    delivery_full_name = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=100)
    delivery_postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.delivery_full_name} - {self.delivery_address}"


class deliveryGuaranteeOptions(models.Model):
    deliver_guarantee = models.BooleanField(default=False)
    text_message = models.BooleanField(default=False)


class deliveryDetailsData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    return_details = models.ForeignKey('returnDetailsModel', on_delete=models.CASCADE)
    delivery_details = models.ForeignKey('deliveryDetailsModel', on_delete=models.CASCADE)
    guarantee_details = models.ForeignKey('deliveryGuaranteeOptions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.return_details} - {self.delivery_details}"


class ServiceUserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_model_data = models.ForeignKey('DeliveryService', on_delete=models.CASCADE)

    sale_applied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.service_model_data.price} - {self.service_model_data}"

class ServicePacketingDeliveryMainModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_booking_data_model = models.ForeignKey('usersBookingData', on_delete=models.CASCADE, null=True, blank=True)
    delivery_data_model = models.ForeignKey('deliveryDetailsData', on_delete=models.CASCADE, null=True, blank=True)
    service_data_model = models.ForeignKey('ServiceUserModel', on_delete=models.CASCADE, null=True, blank=True)
    serviceModelInfo = models.ForeignKey('ServiceModel', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.user_booking_data_model} - {self.delivery_data_model} - {self.service_data_model}"

