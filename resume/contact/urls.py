from django.urls import path
from . import views



app_name = 'contact'

urlpatterns = [
   path('', views.index, name='home'),
   # path('', views.ContactForm.as_view(), name='home'),
]