"""Webcartes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from main import views
from django.urls import include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # Replace PortfolioList for WebList
    path("", views.IndexList.as_view(template_name='html/index.html'), name="index"),
    path("home/", views.IndexList.as_view(template_name='html/index.html'), name="home"),
    path('blog/', views.BlogList.as_view(template_name='html/blog.html'), name="blog"),
    path('download/', views.DownloadList.as_view(template_name='html/download.html'), name="download"),
    path('download_archive/', views.DownloadArchiveList.as_view(template_name='html/download_archive.html'), name="download_archive"),
    path('faq/', views.FaqList.as_view(template_name='html/faq.html'), name="faq"),
    path('wiki/', views.WikiList.as_view(template_name='html/wiki.html'), name="wiki"),
    path('wiki/game/<int:pk>/<str:title>/', views.GameDetail.as_view(template_name='html/game.html'), name='info_game'),
    path('source/', views.SourceList.as_view(template_name='html/source.html'), name="source"),
    path('donate/', views.DonateList.as_view(template_name='html/donate.html'), name="donate"),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
