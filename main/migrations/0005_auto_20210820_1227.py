# Generated by Django 3.1.12 on 2021-08-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_game_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='difficulty',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Unspecified', 'Unspecified')], default='Unspecified', max_length=11),
        ),
    ]
