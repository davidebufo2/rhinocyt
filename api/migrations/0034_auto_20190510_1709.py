# Generated by Django 2.2 on 2019-05-10 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_anamnesis_valv_nas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnesis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anamnesis', to='api.Patient'),
        ),
        migrations.DeleteModel(
            name='Diagnosis',
        ),
    ]
