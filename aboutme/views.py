from django.shortcuts import render, get_object_or_404


# Create your views here.
from aboutme.models import AboutMe


def aboutme_view(request):
    aboutme = get_object_or_404(AboutMe, pk=1)
    return render(request, 'aboutme/index.html', context={'aboutme': aboutme})


def contactme_view(request):
    if request.method == 'POST':
        name = request.POST.get('NAME')

    else:
        aboutme_view(request)
