# Generated by Django 3.0 on 2020-07-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('firstname', models.CharField(max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('pin', models.CharField(max_length=30, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]