# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name=b'IP Address')),
                ('username', models.CharField(null=True, max_length=255)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name=b'HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name=b'Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('get_data', models.TextField(verbose_name=b'GET Data')),
                ('post_data', models.TextField(verbose_name=b'POST Data')),
                ('failures_since_start', models.PositiveIntegerField(verbose_name=b'Failed Logins')),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name=b'IP Address')),
                ('username', models.CharField(null=True, max_length=255)),
                ('trusted', models.BooleanField(default=False)),
                ('http_accept', models.CharField(max_length=1025, verbose_name=b'HTTP Accept')),
                ('path_info', models.CharField(max_length=255, verbose_name=b'Path')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('logout_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-attempt_time'],
                'abstract': False,
            },
        ),
    ]

