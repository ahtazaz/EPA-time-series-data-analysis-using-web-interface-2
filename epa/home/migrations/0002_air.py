# Generated by Django 3.1.5 on 2021-01-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='air',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=60)),
                ('b', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
