# Generated by Django 3.0.2 on 2020-03-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
