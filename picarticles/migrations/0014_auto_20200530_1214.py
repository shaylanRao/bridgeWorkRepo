# Generated by Django 2.2.12 on 2020-05-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picarticles', '0013_remove_photo_shirt_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='article',
            field=models.CharField(max_length=50),
        ),
    ]
