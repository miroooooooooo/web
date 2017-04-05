# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-05 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_user_ignored_competitions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(help_text='Do pol\xed\u010dka nap\xed\u0161te skratku, \u010das\u0165 n\xe1zvu alebo adresy \u0161koly a n\xe1sledne vyberte spr\xe1vnu mo\u017enos\u0165 zo zoznamu. Pokia\u013e va\u0161a \u0161kola nie je v&nbsp;zozname, vyberte "In\xe1 \u0161kola" a&nbsp;po\u0161lite n\xe1m e-mail.', null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.School', verbose_name='\u0161kola'),
        ),
    ]
