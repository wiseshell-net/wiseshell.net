from django.contrib import admin
from .models import Game, GameVariant, GameObjective

# Register your models here.

class GameObjectiveInline(admin.TabularInline):
    list_display = ('get_game', 'objective')
    model = GameObjective
    def get_game(self, obj):
        return obj.game.title


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
                'title', 'published_by', 'origin', 'type', 'players', 'number_of_cards', 'deck', 'play', 'playing_time', 'description', 'visible'
            ),
        }),
        ("Supported Features", {
            "fields": (
                'documentation', 'supported_rules', 'single_player', 'multiplayer', 'notes'
            ),
        }),
    )
    inlines = [
        GameObjectiveInline,
        #GameVariantInline
    ]

admin.site.register(Game, GameAdmin)