# Generated by Django 2.2.6 on 2019-10-22 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191022_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='slug',
        ),
    ]
