from django.contrib import admin
from .models import Game, GameObjective

# Register your models here.

class GameObjectiveInline(admin.TabularInline):
    list_display = ('get_game', 'objective')
    model = GameObjective
    def get_game(self, obj):
        return obj.game.title

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
    ]

admin.site.register(Game, GameAdmin)