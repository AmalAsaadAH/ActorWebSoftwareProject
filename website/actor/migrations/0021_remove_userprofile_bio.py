# Generated by Django 2.0.1 on 2018-02-06 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0020_auto_20180205_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
    ]
