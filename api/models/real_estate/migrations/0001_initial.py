# Generated by Django 3.1.4 on 2021-01-21 18:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('zigbang_link', models.URLField(blank=True, null=True)),
                ('dabang_link', models.URLField(blank=True, null=True)),
                ('naver_estate_link', models.URLField(blank=True, null=True)),
                ('peterpan_link', models.URLField(blank=True, null=True)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broker.broker')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
