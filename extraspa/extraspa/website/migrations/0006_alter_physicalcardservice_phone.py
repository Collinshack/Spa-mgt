# Generated by Django 5.0.1 on 2024-02-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_purchased_frequency_physicalcardservice_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalcardservice',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
