# Generated by Django 2.2.12 on 2020-05-21 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='front_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('videofile', models.FileField(null=True, upload_to='blog/static/images/front_photos', verbose_name='')),
            ],
        ),
    ]
