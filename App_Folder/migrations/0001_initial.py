# Generated by Django 4.1.1 on 2022-11-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NippoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='タイトル')),
                ('content', models.TextField(max_length=1000, verbose_name='内容')),
                ('public', models.BooleanField(default=False, verbose_name='公開する')),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('saved', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
