# Generated by Django 5.1.6 on 2025-03-12 09:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camerashop', '0007_product_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
