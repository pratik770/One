from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'moon.html' )

def album(request):
    return HttpResponse("This is Photo Page")