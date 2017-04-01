# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-16 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170916_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='akcia'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='going',
            field=models.BooleanField(default=False, verbose_name='z\xfa\u010dastnil sa'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='going',
            field=models.BooleanField(default=True, verbose_name='z\xfa\u010dastnil sa'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='type',
            field=models.SmallIntegerField(choices=[(0, '\xfa\u010dastn\xedk'), (1, 'n\xe1hradn\xedk'), (2, 'ved\xfaci')], default=0, verbose_name='typ pozvania'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='sites',
            field=models.ManyToManyField(blank=True, to='sites.Site'),
        ),
    ]