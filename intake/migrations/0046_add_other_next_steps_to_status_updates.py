# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0045_add_is_active_to_template_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusupdate',
            name='other_next_step',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='statusupdate',
            name='additional_information',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='statusupdate',
            name='next_steps',
            field=models.ManyToManyField(blank=True, to='intake.NextStep'),
        ),
    ]