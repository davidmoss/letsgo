from django.urls import include, path

urlpatterns = [
    path('', include("picker.urls", namespace="picker")),
]
