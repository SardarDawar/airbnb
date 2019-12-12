# Generated by Django 2.2.6 on 2019-12-11 00:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Trip Content',
                'ordering': ['-created_at', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination', models.CharField(max_length=100)),
                ('Max_Budget', models.IntegerField()),
                ('Number_of_days', models.IntegerField()),
                ('title', models.CharField(max_length=10)),
                ('Social_media_links', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'User Data',
                'ordering': ['-created_at', '-updated'],
            },
        ),
    ]
