# Generated by Django 2.0.1 on 2018-01-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipespost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipespost',
            name='foodimage',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
