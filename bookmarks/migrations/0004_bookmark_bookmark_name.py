# Generated by Django 2.2.6 on 2019-10-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20191020_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='bookmark_name',
            field=models.CharField(default='Noname', max_length=50),
            preserve_default=False,
        ),
    ]