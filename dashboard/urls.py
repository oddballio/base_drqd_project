"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^admin/rq/', include('django_rq_dashboard.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', lambda x: HttpResponseRedirect(reverse('admin:index'))),
]
urlpatterns += staticfiles_urlpatterns()
admin.site.site_header = u'Redis Administration'
