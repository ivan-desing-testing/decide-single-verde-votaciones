# Generated by Django 2.0 on 2021-01-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_auto_20210113_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='themeVotation',
            field=models.CharField(blank=True, choices=[('El', 'Electoral'), ('Si', 'Self-interest'), ('Kw', 'Knowledge'), ('Ts', 'Testing'), ('Su', 'Survey')], max_length=4, null=True),
        ),
    ]
