from django.shortcuts import render
# Create your views here.


def index(request):

    return render(request, 'index.html', {
        'title': 'Inicio'
    })


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html', {
        'title': 'Sobre nosotros'
    })

def contacto(request):
    return render(request, 'contacto.html', {
        'title': 'Contacto'
    })