from django import forms
from .models import ContactForm, Flan
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

# class ContactFormForm(forms.Form):
#     customer_email = forms.EmailField(label="Correo")
#     customer_name = forms.CharField(max_length=64, label='Nombre')
#     message = forms.CharField(label="Mensaje")

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        widgets = {
            'customer_email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'correo@dominio.cl'}),
            'customer_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
        }

class AuthenticationFormWithWidgets(AuthenticationForm):
    username = UsernameField(label=_("Nombre de usuario"), widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control', 'placeholder':'Nombre de usuario'}))
    password = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control', 'placeholder':'*****************'}),
    )

class FlanModelForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name', 'description', 'image_url', 'is_private']
        # 'flan_uuid' : forms.UUIDField(attrs={'class':'form-control'}),
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
            'image_url' : forms.URLInput(attrs={'class':'form-control', 'placeholder':'http://www.dominio.cl/imagen.png', 'pattern': '/.*\.png|.*\.jpeg|.*\.jpg|.*\.gif|.*\.webp/'}),
            'is_private' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }