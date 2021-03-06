# Generated by Django 3.1.4 on 2021-01-28 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
        ('client', '0001_initial'),
        ('client_tour', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienttour',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
        migrations.AlterField(
            model_name='clienttour',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour'),
        ),
    ]
