from django.shortcuts import render

from DjangoWebBasics.cities.models import Person


def index(req):
    context = {
        'name': 'Gosho',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
