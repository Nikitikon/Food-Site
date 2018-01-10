from django.contrib import admin
from .models import RecipesPost, LikeDislike, Categoey, Menu, Kitchens

# Register your models here.
admin.site.register(RecipesPost)
admin.site.register(Categoey)
admin.site.register(Menu)
admin.site.register(Kitchens)
admin.site.register(LikeDislike)