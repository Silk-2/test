from django.urls import path
from . import views

urlpatterns = [
    path('<str:id_value>', views.get_balance),
    path('<str:id_value>/operation', views.deposit_and_withdraw),
]
