# Generated by Django 2.2.5 on 2019-09-04 05:58

import autoslug.fields
from django.db import migrations, models
import main.notify.models.request


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('read', models.BooleanField(default=False, verbose_name='Is read')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('body', models.TextField(verbose_name='Description')),
                ('href', models.TextField(blank=True, verbose_name='Extra Link')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'Notifications',
                'verbose_name': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='NotificationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('body', models.TextField(verbose_name='Description')),
                ('file', models.FileField(blank=True, null=True, upload_to=main.notify.models.request._handle_notification_file, verbose_name='File')),
                ('staff_only', models.BooleanField(default=False, verbose_name='User Staff Only')),
                ('requesttype', models.CharField(choices=[('general', 'General'), ('custom', 'Custom')], default='general', max_length=24, verbose_name='Request Type')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Received user Count')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'Notification Requests',
                'verbose_name': 'Notification Request',
            },
        ),
    ]
