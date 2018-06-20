from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def disp(request):
    return render(request, 'C:/Users/gupta/Desktop/final/users/templates/about.html')