# Generated by Django 5.0.1 on 2024-02-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code_thhp', models.IntegerField(default=404)),
                ('port_site', models.IntegerField(default=80)),
                ('update_at', models.DateField(auto_now=True)),
                ('created_ar', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
