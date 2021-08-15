from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Project

# Create your views here.
class PortfolioList(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context["projects"] = projects
        return context

class BlogList(TemplateView):
    template_name = "blog.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DownloadList(TemplateView):
    template_name = "download.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DownloadArchiveList(TemplateView):
    template_name = "download_archive.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FaqList(TemplateView):
    template_name = "faq.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class WikiList(TemplateView):
    template_name = "wiki.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SourceList(TemplateView):
    template_name = "source.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DonateList(TemplateView):
    template_name = "donate.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context