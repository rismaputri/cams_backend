# Generated by Django 2.2.6 on 2019-10-30 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0002_auto_20191030_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gaji',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
