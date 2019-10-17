# Generated by Django 2.2 on 2019-05-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190507_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellextraction',
            name='esinophil_num',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cellextraction',
            name='lymphocye_num',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cellextraction',
            name='mastocyte_num',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cellextraction',
            name='mucipara_num',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cellextraction',
            name='neutrophil_num',
            field=models.SmallIntegerField(default=0),
        ),
    ]