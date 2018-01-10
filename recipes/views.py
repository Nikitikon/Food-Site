from django.shortcuts import render, render_to_response
from .models import RecipesPost
from  django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def main_page(request):
    recipes_post = RecipesPost.objects.filter(published_date__lte=timezone.now()).order_by('-recipe_rating')[0:6]
    return render(request, 'mainPage/main_page.html', {'recipes' : recipes_post})

def recipes_list(request):
