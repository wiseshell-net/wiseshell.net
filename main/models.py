from django.db import models
from tinymce.models import HTMLField

# Create your models here.

# Wiki
# Like this: https://en.wikipedia.org/wiki/Escoba

# Image will go into main board
class Game(models.Model):
    NOTES_DESCRIPTION = "Separate your explanation in paragraphs if needed."
    DIFFICULTY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Unspecified', 'Unspecified')
    )
    
    title = models.CharField(max_length=400, help_text="If you need some clue about how to fill this, please see https://en.wikipedia.org/wiki/Escoba")
    published_by = models.CharField(max_length=400)
    origin = models.CharField(max_length=400)
    type = models.CharField(max_length=400)
    players = models.CharField(max_length=400)
    number_of_cards = models.CharField(max_length=100)
    deck = models.CharField(max_length=400)
    play = models.CharField(max_length=400, help_text="Clockwise, Counterclockwise, Unspecified...", default="Unspecified")
    playing_time = models.CharField(max_length=400)
    difficulty = models.CharField(max_length=11, choices=DIFFICULTY_CHOICES, default="Unspecified")
    description = HTMLField(blank=True, null=True, help_text=NOTES_DESCRIPTION)
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
    NOTES_FIELD = "<p>Please insert the explanation here. You can put bullets to clarify your explanation: </p><ul><li>This rule is not implemented</li><li>This feature needs to be polished</li></ul>"
    documentation = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    supported_rules = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    single_player = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    multiplayer = models.CharField(max_length=11, choices=SUPPORT_CHOICES)
    notes = HTMLField(blank=True, null=True, help_text=NOTES_FIELD)

# Each part belongs to a section of the game regulations
class GameRegulation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="orig_game")
    title = models.CharField(max_length=100, help_text="If you need some clue about how to fill this, please see https://en.wikipedia.org/wiki/Escoba")
    description = HTMLField()
    image = models.ImageField(upload_to = 'game_photo/', blank=True, null=True)
    caption = models.CharField(max_length=1000, blank=True, null=True)
    alt = models.CharField(max_length=400, blank=True, null=True)

class GameVariant(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="original_game")
    variant = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_variant")