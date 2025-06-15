from django.urls import path
from .views import classify_image

urlpatterns = [
    path('predict/', classify_image, name="classify_image")
]   