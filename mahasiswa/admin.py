from django.contrib import admin
from mahasiswa.models import Mahasiswa
# Register your models here.

class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['no','nama', 'nim', 'ttl', 'email', 'foto']
    search_fields = ['nim','nama']
    

admin.site.register(Mahasiswa, MahasiswaAdmin)