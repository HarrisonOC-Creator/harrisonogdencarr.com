"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from projects import views
from django.contrib.sitemaps.views import sitemap
from projects.sitemaps import StaticViewSitemap
from django.http import HttpResponse
from django.views.generic import RedirectView



sitemaps_dict = {
    'static': StaticViewSitemap,
    }
def bing_verification(request):
    return HttpResponse(open("/home/harrisonogdencarr/www_harrisonogdencarr_com/BingSiteAuth.xml").read(),
                        content_type="text/xml")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.project_list, name="project_list"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
    path("demo/api/", views.demo_api, name="demo_api"),  # AJAX endpoint
    path("dog-breed-classifier/", views.dog_breed_demo, name="dog_breed_classifier"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),
    path("BingSiteAuth.xml", bing_verification),
    path("favicon.ico", RedirectView.as_view(url="/static/projects/images/favicon.png")),
    path("favicon.png", RedirectView.as_view(url="/static/projects/images/favicon.png")),
    path("favicon-192.png", RedirectView.as_view(url="/static/projects/images/favicon-192.png")),
    path("robots.txt", RedirectView.as_view(url="/static/robots.txt")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

