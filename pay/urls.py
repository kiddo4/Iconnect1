from django.urls import path
from pay import views
urlpatterns=[
     path('paypal/',views.pay, name='pay')

]