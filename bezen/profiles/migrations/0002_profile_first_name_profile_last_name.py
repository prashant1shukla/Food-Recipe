# Generated by Django 4.1.2 on 2022-10-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Ram', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Shukla', max_length=100),
        ),
    ]
