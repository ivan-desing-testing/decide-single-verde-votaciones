# Generated by Django 2.0 on 2021-01-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_voting_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='preference',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Mid'), ('L', 'Low')], max_length=4),
        ),
    ]
