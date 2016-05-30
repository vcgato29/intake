# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0003_auto_20151126_1523'),
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('invitation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invitations.Invitation')),
            ],
            bases=('invitations.invitation',),
        ),
        migrations.AlterField(
            model_name='organization',
            name='blurb',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='invitation',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_accounts.Organization'),
        ),
    ]
