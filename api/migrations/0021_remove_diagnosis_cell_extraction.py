# Generated by Django 2.2 on 2019-05-08 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190508_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosis',
            name='cell_extraction',
        ),
    ]
