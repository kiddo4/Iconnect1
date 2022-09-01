from django.urls import path

from . import views

urlpatterns = [
    path('cryptopay/', views.home_view, name='cryptohome'),
    path('success/', views.success_view, name='cryptosuccess'), # new
    path('cancel/', views.cancel_view, name='cryptocancel'), # new
    path('webhook/', views.coinbase_webhook),  # new

]