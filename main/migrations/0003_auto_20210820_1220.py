# Generated by Django 3.1.12 on 2021-08-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210820_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='number_of_cards',
            field=models.CharField(max_length=100),
        ),
    ]
