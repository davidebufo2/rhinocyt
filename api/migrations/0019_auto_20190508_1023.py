# Generated by Django 2.2 on 2019-05-08 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190508_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anamnsesis', to='api.Patient'),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='api.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
