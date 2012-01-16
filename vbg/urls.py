# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import ListView
from firm_app.views import hello
from firm_app.models import Firm, Rubric

admin.autodiscover()

firm_info= {
    "queryset": Firm.objects.all(),
    }

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListView.as_view(model=Firm)),
    #url(r'^catalog/<slug>$',hello), тут должна быть переменная, <slug>  которую нам надо передать в представление
    #url(r'^vbg/', include('vbg.foo.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
