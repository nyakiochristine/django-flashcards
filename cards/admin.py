from django.contrib import admin
# Register your models here.
from .models import Card_Set,Card

admin.site.register(Card)
admin.site.register(Card_Set)

