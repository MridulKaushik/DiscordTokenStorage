from django.urls import path
from .views import get_Token

urlpatterns = [
    path('', get_Token, name="token")
]
