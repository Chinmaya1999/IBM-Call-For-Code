# Generated by Django 3.0 on 2020-07-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20200719_1306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feed',
            new_name='NewsFeed',
        ),
    ]