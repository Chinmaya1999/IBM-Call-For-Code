# Generated by Django 3.0.8 on 2020-07-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20200722_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='done',
            field=models.IntegerField(null=True),
        ),
    ]
