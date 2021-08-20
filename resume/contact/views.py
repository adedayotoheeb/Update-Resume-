from os import name
from .models import Contact
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
# from django.contrib.messages import constants as messages

# Create your views here.

def index(request):
    if request.method =='POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank You, Your Message was sent sucessfully')
    else:
        contact_form = ContactForm()
    context = {'con': contact_form }
    return render(request, 'contact/index.html', context )

# class ContactForm(CreateView, ListView):
#     model= Contact
#     fields = ['name', 'email', 'message',  ]
#     template_name = 'contact/index.html'
#     success_url = reverse_lazy('contact:home')
