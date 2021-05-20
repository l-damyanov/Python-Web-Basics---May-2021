from django.http import HttpResponse
from django.shortcuts import render

from DjangoWebBasics.cities.models import Person


def index(req):
    context = {
        'name': 'Gosho',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def list_phones(req):
    # return HttpResponse('Phones list')
    context = {
        'phones': [
            {
                'name': 'Galaxy S5000',
                'quantity': 3
            },
            {
                'name': 'Xiaomi Readmi T9',
                'quantity': 3
            },
            {
                'name': 'iPhone 12',
                'quantity': 3
            },
        ]
    }
    context['message'] = 'Phones list'
    return render(req, 'phones.html', context)

