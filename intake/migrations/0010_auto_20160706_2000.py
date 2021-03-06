# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import intake.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0009_auto_20160615_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationSentLogEntry',
            fields=[
                ('applicationlogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='intake.ApplicationLogEntry')),
                ('contact_info', intake.models.fields.ContactInfoJSONField(default=dict)),
            ],
            bases=('intake.applicationlogentry',),
        ),
        migrations.AlterField(
            model_name='applicationlogentry',
            name='event_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'opened'), (2, 'referred'), (3, 'processed'), (4, 'deleted'), (5, 'sent confirmation')]),
        ),
    ]
