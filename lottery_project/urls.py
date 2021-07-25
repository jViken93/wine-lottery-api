from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lottery_api import views

router = DefaultRouter()
router.register('LotteryRegistration', views.LotteryRegistrationViewSet)
router.register('tickets', views.ticketsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
