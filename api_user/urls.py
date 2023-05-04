from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_dm import views

app_name = 'user'

router = DefaultRouter()

urlpatterns = [
    path('',include(router.urls))
]
