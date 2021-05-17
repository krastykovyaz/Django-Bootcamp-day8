from django.urls import path, include
from image_app.views import LoadImage


urlpatterns = [
    path('', LoadImage.as_view(), name='index'),
]