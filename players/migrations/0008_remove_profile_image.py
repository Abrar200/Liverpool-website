# Generated by Django 3.1.7 on 2021-05-03 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]
