# Generated by Django 3.1.7 on 2021-05-03 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
