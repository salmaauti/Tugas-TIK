from django.contrib import admin
from staf.models import Staf
# Register your models here.

class StafAdmin(admin.ModelAdmin):
    list_display = ['no', 'nip','nama', 'jabatan']
    search_fields = ['nip','nama']
    

admin.site.register(Staf, StafAdmin)