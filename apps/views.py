from django.shortcuts import render
from apps.models import Intro, Abt, Portfolio, Services, Testimonials, Clients


def index(request):
    queryset = Intro.objects, Abt.objects,  Portfolio.objects, Services.objects,  Testimonials.objects,  Clients.objects
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)


def brand(request):
    return render(request, 'brand.html', {})


def design(request):
    return render(request, 'design.html', {})


def dev(request):
    return render(request, 'dev.html',  {})


def ui(request):
    return render(request, 'ui.html',  {})
