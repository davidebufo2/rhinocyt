# Generated by Django 2.2 on 2019-05-08 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190508_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell_extraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='api.CellExtraction')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='api.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
