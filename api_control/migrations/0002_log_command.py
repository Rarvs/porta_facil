# Generated by Django 5.1.5 on 2025-02-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='command',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
