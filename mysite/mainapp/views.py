from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/homepage.html')
# Create your views here.

def contact(request):
    return render(request, 'mainapp/basic.html' , {'values' : ['Если у вас есть вопросы, то задавайте их мне по телефону', '(000) 394-32-44', 'email@mail.ru']})
