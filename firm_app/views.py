# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Здравствуй, Мир, <h1>Сука</h1>")