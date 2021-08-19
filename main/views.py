from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Game, GameObjective

# Create your views here.

class IndexList(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

class WikiList(TemplateView):
    template_name = "wiki.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        games = Game.objects.all()
        context["games"] = games
        return context

class GameDetail(DetailView):
    model = Game
    template_name="html/game.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        game = Game.objects.get(pk=pk)
        #objectives = GameObjective.objects.filter(id=pk)
        #import pdb; pdb.set_trace()
        context["game"] = game
        #context["objectives"] = objectives
        return context