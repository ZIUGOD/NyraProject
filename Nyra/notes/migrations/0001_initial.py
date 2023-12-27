# Generated by Django 5.0 on 2023-12-26 01:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='título')),
                ('text', ckeditor.fields.RichTextField(unique=True, verbose_name='Texto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at: ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at: ')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Notas',
                'ordering': ['-updated_at'],
            },
        ),
    ]
