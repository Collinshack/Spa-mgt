# Generated by Django 5.0.1 on 2024-02-04 02:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electroniccardservice',
            name='uniquec',
        ),
        migrations.RemoveField(
            model_name='electroniccardsum',
            name='uniquec',
        ),
        migrations.RemoveField(
            model_name='physicalcardservice',
            name='uniquec',
        ),
        migrations.RemoveField(
            model_name='physicalcardsum',
            name='uniquec',
        ),
        migrations.AddField(
            model_name='electroniccardservice',
            name='unique_code',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electroniccardsum',
            name='unique_code',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physicalcardservice',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physicalcardservice',
            name='unique_code',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physicalcardsum',
            name='unique_code',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='electroniccardservice',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.service'),
        ),
        migrations.AlterField(
            model_name='electroniccardservice',
            name='spa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.spa'),
        ),
        migrations.AlterField(
            model_name='electroniccardservice',
            name='type',
            field=models.CharField(choices=[('service', 'Service'), ('sum', 'Sum')], default='sum', max_length=10),
        ),
        migrations.AlterField(
            model_name='electroniccardsum',
            name='spa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.spa'),
        ),
        migrations.AlterField(
            model_name='physicalcardservice',
            name='spa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.spa'),
        ),
        migrations.AlterField(
            model_name='physicalcardservice',
            name='type',
            field=models.CharField(choices=[('service', 'Service'), ('sum', 'Sum')], default='sum', max_length=10),
        ),
        migrations.AlterField(
            model_name='physicalcardsum',
            name='spa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.spa'),
        ),
        migrations.AlterField(
            model_name='spa',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spa_admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
