# Generated by Django 2.0 on 2021-01-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='preference',
            field=models.CharField(blank=True, choices=[('H', 'High'), ('M', 'Mid'), ('L', 'Low')], max_length=4, null=True),
        ),
    ]
