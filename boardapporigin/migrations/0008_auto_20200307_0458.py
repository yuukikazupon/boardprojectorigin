# Generated by Django 3.0.2 on 2020-03-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapporigin', '0007_auto_20200306_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='read_text',
            field=models.CharField(default='a', max_length=50),
        ),
    ]