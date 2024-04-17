from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from seller.models import *

def index(request):
  product_list = TravelProduct.objects.all
  context = {
    'product_list':product_list
  }
  return render(request, 'home.html', context)

class UserCreateView(generic.CreateView):
  template_name = 'registration/register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('register_done')

class UserCreateDoneTV(generic.TemplateView):
  template_name = 'registration/register_done.html'

