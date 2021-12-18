from django.urls import path
from footimgapp.views import FootimgCreateView, FootimgUpdateView


app_name = 'footimgapp'

urlpatterns = [
    path('create/', FootimgCreateView.as_view(), name='create'),
    path('update/<int:pk>', FootimgUpdateView.as_view(), name='update'),
]