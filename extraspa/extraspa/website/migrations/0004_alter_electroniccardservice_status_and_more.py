# Generated by Django 5.0.1 on 2024-02-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_electroniccardservice_unique_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electroniccardservice',
            name='status',
            field=models.CharField(choices=[('Активен', 'Активен'), ('Потрачен', 'Потрачен')], default='Активен', max_length=10),
        ),
        migrations.AlterField(
            model_name='electroniccardsum',
            name='status',
            field=models.CharField(choices=[('Активен', 'Активен'), ('Потрачен', 'Потрачен')], default='Активен', max_length=10),
        ),
        migrations.AlterField(
            model_name='electroniccardsum',
            name='type',
            field=models.CharField(choices=[('service', 'Service'), ('sum', 'Sum')], default='sum', max_length=10),
        ),
        migrations.AlterField(
            model_name='physicalcardservice',
            name='status',
            field=models.CharField(choices=[('Активен', 'Активен'), ('Потрачен', 'Потрачен')], default='Активен', max_length=10),
        ),
        migrations.DeleteModel(
            name='PhysicalCardSum',
        ),
    ]
