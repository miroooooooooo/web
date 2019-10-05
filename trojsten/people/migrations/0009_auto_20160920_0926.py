# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 07:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("people", "0008_userpropertykey_regex")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=30, verbose_name="first name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=30, verbose_name="last name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True,
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=30,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[\\w.@+-]+$",
                        "Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.",
                    )
                ],
                verbose_name="username",
            ),
        ),
    ]
