# Generated by Django 2.2.24 on 2025-04-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20250409_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(null=True),
        ),
    ]
