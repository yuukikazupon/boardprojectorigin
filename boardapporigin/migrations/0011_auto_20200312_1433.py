# Generated by Django 3.0.2 on 2020-03-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0010_auto_20200312_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
