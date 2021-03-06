# Generated by Django 2.0.1 on 2018-01-10 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20180110_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')])),
            ],
        ),
        migrations.RenameModel(
            old_name='RecopesPost',
            new_name='RecipesPost',
        ),
        migrations.AddField(
            model_name='likedislike',
            name='recipes_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.RecipesPost'),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
