# Generated by Django 3.0.2 on 2020-03-04 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0003_auto_20200304_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmodel',
            old_name='memo',
            new_name='content',
        ),
    ]
