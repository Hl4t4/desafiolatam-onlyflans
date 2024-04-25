from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Flan, ContactForm
from .forms import ContactFormForm

# Create your views here.

def index_view(request):
    flanes = {"flanes":Flan.objects.all()}
    flanes_publicos = {"flanes":Flan.objects.filter(is_private=False)}
    return render(request, "index.html", flanes_publicos)

def about_view(request):
    return render(request, "about.html", {})

def welcome_view(request):
    flanes_privados = {"flanes":Flan.objects.filter(is_private=True)}
    return render(request, "welcome.html", flanes_privados)

def contact_view(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()
    
    return render(request, "contact.html", {'form': form})

def contact_success_view(request):
    return render(request, "contact_success.html", {})
