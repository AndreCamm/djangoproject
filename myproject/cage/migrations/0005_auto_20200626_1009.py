# Generated by Django 3.0.7 on 2020-06-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cage', '0004_monster_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='monster_location',
        ),
        migrations.AddField(
            model_name='location',
            name='monsters',
            field=models.ManyToManyField(to='cage.Monster'),
        ),
    ]