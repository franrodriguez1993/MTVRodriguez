from django.contrib import admin
from familiaresApp.models import Familiares
# Register your models here.

class FamiliaresAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','edad','email')

admin.site.register(Familiares,FamiliaresAdmin)
    