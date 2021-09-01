from django.contrib import admin
from .models import Game, GameVariant, GameRegulation

# Register your models here.

class GameRegulationInline(admin.TabularInline):
    list_display = ('get_game', 'objective')
    model = GameRegulation
    def get_game(self, obj):
        return obj.game.title
    fieldsets = (
        ("Game Regulations", {
            "fields": (
                'title', 'description', 'image', 'caption'
            ),
        }),
    )
    def get_form(self, request, obj=None, **kwargs):
        form = super(GameRegulation, self).get_form(request, obj, **kwargs)
        form.base_fields['description'].widget.attrs['style'] = 'width: 45em;'
        return form

"""
class GameVariantInline(admin.TabularInline):
    list_display = ('get_game', 'get_game_variant')
    model = GameVariant
    def get_game(self, obj):
        return obj.game.title

    def get_game_variant(self, obj):
        return obj.variant.title
"""

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_by', 'last_modified', 'visible')
    fieldsets = (
        ("General", {
            "fields": (
                'title', 'published_by', 'origin', 'type', 'players', 'number_of_cards', 'deck', 'play', 'playing_time', 'difficulty', 'description', 'visible'
            ),
        }),
        ("Supported Features", {
            "fields": (
                'documentation', 'supported_rules', 'single_player', 'multiplayer', 'notes'
            ),
        }),
    )
    inlines = [
        GameRegulationInline,
        #GameVariantInline
    ]

admin.site.register(Game, GameAdmin)