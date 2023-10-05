from django.urls import path
from .views import user_form, many_fields_form, Product

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('product/', Product, name='product'),
]
