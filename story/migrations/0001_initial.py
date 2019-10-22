# Generated by Django 2.2.6 on 2019-10-22 14:20

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0008_remove_story_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storyline',
            fields=[
                ('story_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Story')),
                ('order', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]