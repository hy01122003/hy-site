"""
Definition of urls for Vocabulary.
"""

from django.conf.urls import include, url
from django.urls import path
from django.contrib import admindocs

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', Vocabulary.views.home, name='home'),
    # url(r'^Vocabulary/', include('Vocabulary.Vocabulary.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    path('home/', include('Vocabulary.home.urls'), name='home'),
]
