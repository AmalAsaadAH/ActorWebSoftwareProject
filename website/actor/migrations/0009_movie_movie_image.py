# Generated by Django 2.0 on 2018-02-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(default='', max_length=1000, upload_to=''),
        ),
    ]
