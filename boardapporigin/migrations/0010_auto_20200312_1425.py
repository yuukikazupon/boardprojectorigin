# Generated by Django 3.0.2 on 2020-03-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0009_auto_20200310_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
