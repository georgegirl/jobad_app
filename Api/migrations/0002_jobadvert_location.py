# Generated by Django 4.1.1 on 2022-09-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobadvert',
            name='location',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
