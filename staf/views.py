from django.shortcuts import render
from staf.models import Staf
# Create your views here.
def staf(request):
    context = {
        'educator': Staf.objects.all()
        
    }
    return render(request,"indexs.html", context)
