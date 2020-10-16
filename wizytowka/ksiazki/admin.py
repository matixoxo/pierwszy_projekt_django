from django.contrib import admin
from .models import Ksiazki, Kategoria, Wydawnictwo
# Register your models here.
admin.site.register(Ksiazki)
admin.site.register(Kategoria)
admin.site.register(Wydawnictwo)