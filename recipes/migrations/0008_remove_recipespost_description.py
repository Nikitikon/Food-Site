# Generated by Django 2.0.1 on 2018-01-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20180110_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipespost',
            name='description',
        ),
    ]
