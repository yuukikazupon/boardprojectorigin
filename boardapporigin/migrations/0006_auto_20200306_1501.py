# Generated by Django 3.0.2 on 2020-03-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0005_auto_20200306_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]
