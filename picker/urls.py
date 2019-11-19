from django.urls import path

from .views import PickerView

app_name = "picker"
urlpatterns = [
    path('', PickerView.as_view()),
]
