from django.contrib import admin
from django.urls import path
from .views import send_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/send_message', send_message, name="send_message"),
]
