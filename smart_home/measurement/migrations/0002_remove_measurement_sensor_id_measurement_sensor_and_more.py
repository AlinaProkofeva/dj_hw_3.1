# Generated by Django 4.1.4 on 2022-12-25 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(db_index=True, max_length=40),
        ),
    ]
