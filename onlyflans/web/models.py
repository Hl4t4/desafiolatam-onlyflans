from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default= uuid.uuid4)
    name = models.CharField(max_length=64, verbose_name = "Nombre")
    description = models.TextField(verbose_name = "Descripcion")
    image_url = models.URLField(verbose_name = "URL de la imagen")
    slug = AutoSlugField(populate_from='name')
    is_private = models.BooleanField(default=False, verbose_name = "¿Es privado?")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=list(User.objects.filter(username = 'desafioLatam'))[0].id)

    class Meta :
        verbose_name = "flan"
        verbose_name_plural = "flanes"

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default= uuid.uuid4, editable=False)
    customer_email = models.EmailField(verbose_name = "Correo")
    customer_name = models.CharField(max_length=64, verbose_name="Nombre")
    message = models.TextField(verbose_name="Mensaje")