# Generated by Django 2.1.9 on 2019-10-06 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contests", "0019_auto_20191005_2320")]

    operations = [
        migrations.AlterField(
            model_name="taskpeople",
            name="role",
            field=models.IntegerField(
                choices=[(0, "opravovateľ"), (1, "vzorákovač"), (2, "recenzovač")],
                verbose_name="funkcia",
            ),
        ),
        migrations.AlterField(
            model_name="taskpeople",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_people",
                to="contests.Task",
                verbose_name="úloha",
            ),
        ),
    ]
