# Generated by Django 5.0.1 on 2024-01-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('amount', models.CharField(max_length=30)),
                ('unique', models.CharField(max_length=30)),
            ],
        ),
    ]
