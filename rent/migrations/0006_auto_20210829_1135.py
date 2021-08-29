# Generated by Django 3.2.6 on 2021-08-29 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_alter_carrent_car'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrent',
            options={'verbose_name': 'car rent', 'verbose_name_plural': 'car rents'},
        ),
        migrations.RemoveField(
            model_name='carrent',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='carrent',
            name='rent_time',
        ),
        migrations.AddField(
            model_name='carrent',
            name='end_rent_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carrent',
            name='start_rent_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carrent',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rent.car', verbose_name='car'),
        ),
    ]
