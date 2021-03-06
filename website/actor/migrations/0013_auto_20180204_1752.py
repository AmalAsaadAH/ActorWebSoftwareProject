# Generated by Django 2.0 on 2018-02-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0012_auto_20180204_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='city',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default=' ', max_length=1000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0, max_length=15),
        ),
    ]
