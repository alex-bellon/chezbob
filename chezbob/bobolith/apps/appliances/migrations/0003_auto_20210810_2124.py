# Generated by Django 3.2.5 on 2021-08-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0002_appliancelink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appliance',
            options={'verbose_name': 'Appliance'},
        ),
        migrations.AlterModelOptions(
            name='appliancelink',
            options={'verbose_name': 'Appliance Link'},
        ),
        migrations.AddField(
            model_name='appliance',
            name='config',
            field=models.JSONField(default=dict, verbose_name='configuration'),
        ),
    ]