# cities.urls
from django.urls import path

from django.views.generic import TemplateView

from DjangoWebBasics.cities.views import index, list_phones

urlpatterns = [
    path('', index),  # /'cities/' + '' = '/cities/'
    path('phones/', list_phones),  # /'cities/' + 'phones/' = '/cities/phones/'
    path('phones2/', TemplateView.as_view(template_name='phones.html')),
]
