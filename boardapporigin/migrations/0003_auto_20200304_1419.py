# Generated by Django 3.0.2 on 2020-03-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0002_auto_20200304_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
