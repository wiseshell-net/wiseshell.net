from django.db import models

# Create your models here.

# Wiki
# Like this: https://en.wikipedia.org/wiki/Escoba

# Image will go into main board
class Game(models.Model):
    title = models.CharField(max_length=400, help_text="If you need some clue about how to fill this, please see https://en.wikipedia.org/wiki/Escoba")
    published_by = models.CharField(max_length=400)
    origin = models.CharField(max_length=400)
    type = models.CharField(max_length=400)
    players = models.CharField(max_length=400)
    number_of_cards = models.IntegerField()
    deck = models.CharField(max_length=400)
    play = models.CharField(max_length=400)
    playing_time = models.CharField(max_length=400)
    description = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)

    # Supported features
    # Only allow Y for Yes, N for No, P for Partial (needs notes) and Unavailable 
    SUPPORT_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('P', 'Partial (need explanation in notes)'),
        ('Unavailable', 'Unavailable')
    )
    documentation = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    supported_rules = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    single_player = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    multiplayer = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    notes = models.TextField(blank=True, null=True)

# This will go into objective
class GameObjective(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_objective")
    objective =  models.TextField()
    image = models.ImageField(upload_to = 'game_photo/', blank=True, null=True)
    caption = models.CharField(max_length=1000, blank=True, null=True)
    alt = models.CharField(max_length=400)