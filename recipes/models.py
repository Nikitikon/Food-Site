from django.db import models
from django.utils import timezone
from PIL import Image
from django.db.models import Sum

# Create your models here.

class RecipesPost(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    instruction = models.TextField(max_length=5000)
    published_date = models.DateTimeField(
        blank=True, null=True)
    foodimage = models.ImageField(
        upload_to = "static/image/UserImage"
        )
    food_category = models.ForeignKey('recipes.Categoey', on_delete=models.CASCADE, null=True, blank=True)
    food_menu = models.ForeignKey('recipes.Menu', on_delete=models.CASCADE, null=True, blank=True)
    food_kitchens  = models.ForeignKey('recipes.Kitchens', on_delete=models.CASCADE, null=True, blank=True)
    food_ingredients = models.TextField(max_length=1000, blank=True)
    recipe_rating = models.DecimalField(max_digits=8, decimal_places=4, default=0.0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Сначала - обычное сохранение
        super(RecipesPost, self).save(*args, **kwargs)
        _MAX_SIZE = 700

        # Проверяем, указан ли логотип
        if self.foodimage:
            filepath = self.foodimage.path
            width = self.foodimage.width
            height = self.foodimage.height

            max_size = max(width, height)

            # Может, и не надо ничего менять?
            if max_size > _MAX_SIZE:
                # Надо, Федя, надо
                image = Image.open(filepath)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),  # Сохраняем пропорции
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                # И не забыть сохраниться
                image.save(filepath)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Categoey(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Kitchens(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(choices=VOTES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    recipes_post = models.ForeignKey('recipes.RecipesPost', on_delete=models.CASCADE)


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0