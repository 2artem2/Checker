# Generated by Django 5.0.1 on 2024-02-07 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DJchecker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='created_ar',
            new_name='created_at',
        ),
    ]
