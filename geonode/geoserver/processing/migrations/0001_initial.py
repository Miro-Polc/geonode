# Generated by Django 3.2.4 on 2021-06-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geonode_resource_processing', '0002_alter_processingworkflowtasks_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleGeoServerProcessingTask',
            fields=[
                ('abstractprocessingtask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='geonode_resource_processing.abstractprocessingtask')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('geonode_resource_processing.abstractprocessingtask',),
        ),
    ]