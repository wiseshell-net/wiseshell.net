# Generated by Django 3.1.12 on 2021-08-20 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210820_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='play',
            field=models.CharField(default='Unspecified', help_text='Clockwise, Counterclockwise, Unspecified...', max_length=400),
        ),
    ]