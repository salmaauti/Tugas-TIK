"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from faperta.views import prodi
from feb.views import prodi1
from fh.views import prodi2
from fisip.views import prodi3
from fk.views import prodi4
from fkip.views import prodi5
from ft.views import prodi6
from pascasarjana.views import prodi7
from kampus.views import prodik
from profil.views import prodip
from dosen.views import dosen
from dosen.views import tambah_dosen
from dosen.views import ubah_dosen
from dosen.views import hapus_dosen
from mahasiswa.views import mahasiswa
from mahasiswa.views import tambah_mahasiswa
from mahasiswa.views import ubah_mahasiswa
from mahasiswa.views import hapus_mahasiswa
from staf.views import staf
from staf.views import tambah_staf
from staf.views import ubah_staf
from staf.views import hapus_staf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', prodi),
    path('feb/', prodi1),
    path('fh/', prodi2),
    path('fisip/', prodi3),
    path('fk/', prodi4),
    path('fkip/', prodi5),
    path('ft/', prodi6),
    path('pascasarjana/', prodi7),
    path('kampus/', prodik),
    path('profil/', prodip),
    path('dosen/', dosen, name="dosen"),
    path('tambah-dosen/', tambah_dosen),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name="ubah_dosen"),
    path('dosen/hapus/<int:id_dosen>', hapus_dosen, name="hapus_dosen"),
    path('mahasiswa/', mahasiswa, name="mahasiswa"),
    path('tambah-mahasiswa/', tambah_mahasiswa),
    path('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name="ubah_mahasiswa"),
    path('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name="hapus_mahasiswa"),
    path('staf/', staf, name="staf"),
    path('tambah-staf/', tambah_staf),
    path('staf/ubah/<int:id_staf>', ubah_staf, name="ubah_staf"),
    path('staf/hapus/<int:id_staf>', hapus_staf, name="hapus_staf"),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)