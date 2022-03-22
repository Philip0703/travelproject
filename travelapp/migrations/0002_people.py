# Generated by Django 3.2.8 on 2021-11-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
    ]
