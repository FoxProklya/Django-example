from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h3> Hello world! </h3>')

def index(request):
    return render(request, 'webexample/button.html')
# Create your views here.
