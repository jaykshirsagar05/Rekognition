# Generated by Django 2.2.1 on 2020-03-28 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='similarfaceinimage',
            name='fileurl',
        ),
    ]
