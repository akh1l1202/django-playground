from django.urls import path
from .views import home, StudentView

urlpatterns = [
    path('fbv/', home, name='home'),
    path('cbv/', StudentView.as_view(), name='student'),
]