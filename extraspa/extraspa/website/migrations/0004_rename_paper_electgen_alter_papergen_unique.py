# Generated by Django 5.0.1 on 2024-01-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_papergen_unique'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paper',
            new_name='ElectGen',
        ),
        migrations.AlterField(
            model_name='papergen',
            name='unique',
            field=models.CharField(max_length=30),
        ),
    ]