from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login

# Create your views here.

def index_view(request):
    flanes = {"flanes":Flan.objects.all()}
    flanes_publicos = {"flanes":Flan.objects.filter(is_private=False)}
    return render(request, "index.html", flanes_publicos)

def about_view(request):
    return render(request, "about.html", {})

@login_required
def welcome_view(request):
    flanes_privados = {"flanes":Flan.objects.filter(is_private=True)}
    return render(request, "welcome.html", flanes_privados)

def contact_view(request):
    if request.method == 'POST':
        # form = ContactFormForm(request.POST)
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        # form = ContactFormForm()
        form = ContactFormModelForm()
    
    return render(request, "contact.html", {'form': form})

def contact_success_view(request):
    return render(request, "contact_success.html", {})

def add_flan_view(request):
    return render(request, "add_flan.html", {})

# class CustomLoginView(LoginView):
#     form_class = AuthenticationFormWithWidgets
#     template_name = "registration/login.html"

# def login_view(request):
#     print("swag")
#     if request.method == 'POST':
#         # form = ContactFormForm(request.POST)
#         form = AuthenticationFormWithWidgets(request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponseRedirect('/')
#     else:
#         # form = ContactFormForm()
#         form = AuthenticationFormWithWidgets()
#     return render(request, "registration/login.html", {'form': form})


