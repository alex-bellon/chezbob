# Generated by Django 3.2.7 on 2021-10-02 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20211002_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity in stock')),
                ('last_updated_at', models.DateTimeField(blank=True, null=True, verbose_name='last updated at')),
                ('last_restocked_at', models.DateTimeField(blank=True, null=True, verbose_name='last updated at')),
                ('sku', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='inventory', to='inventory.product', verbose_name='SKU')),
            ],
        ),
    ]
