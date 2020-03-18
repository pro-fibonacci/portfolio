from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def brand(request):
    return render(request, 'brand.html', {})


def design(request):
    return render(request, 'design.html', {})


def dev(request):
    return render(request, 'dev.html',  {})


def ui(request):
    return render(request, 'ui.html',  {})
