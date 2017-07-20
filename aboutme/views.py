from django.shortcuts import render, get_object_or_404


# Create your views here.
from aboutme.models import AboutMe, ContactMe


def aboutme_view(request):
    aboutme = get_object_or_404(AboutMe, pk=1)
    return render(request, 'aboutme/index.html', context={'aboutme': aboutme})


def contactme_view(request):
    aboutme = get_object_or_404(AboutMe, pk=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contactme_obj = ContactMe(name=name, email=email, phone=phone, message=message)
        contactme_obj.save()
    return render(request, 'aboutme/index.html', context={'aboutme': aboutme})
