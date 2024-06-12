from django.contrib import admin
from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path('', views.index, name="index"),
    path('select_service/<int:user_service_id>/', views.select_service, name="select_service"),
    path('details_view/<int:main_model_id>/', views.details_view, name="details_view"),
    path('details_view2/<int:main_model_id>', views.details_view2, name="details_view2"),
    path('details_summary/', views.details_summary, name="details_summary"),
    path('successful_order/', views.successful_order, name='successful_order'),
    path('order_destinations/', views.orderDestination, name='orderDestination'),
]
