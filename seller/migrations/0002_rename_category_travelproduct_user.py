# Generated by Django 5.0.3 on 2024-04-17 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelproduct',
            old_name='category',
            new_name='user',
        ),
    ]
