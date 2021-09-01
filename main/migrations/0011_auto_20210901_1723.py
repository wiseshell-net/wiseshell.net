# Generated by Django 3.1.12 on 2021-09-01 15:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210901_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameregulation',
            name='description',
            field=tinymce.models.HTMLField(help_text='<p>Please insert the explanation here. If you insert a table, please make sure that the font is << System Font >> and there is no font styling (font-size: small or font-size:16px...) in each row when saving it.</p><p><b>Note:</b> In case there is such issue, you can install FoxReplace on Firefox, search each font style and replacing them all by nothing.</p>'),
        ),
    ]
