from django.shortcuts import render, render_to_response
from .models import RecipesPost
from  django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    recipes_post = RecipesPost.objects.filter(published_date__lte=timezone.now()).order_by('-recipe_rating')[0:6]
    return render(request, 'mainPage/main_page.html', {'recipes' : recipes_post})

def recipes_list(request):
    context = {}
    # Забираем все опубликованные статье отсортировав их по дате публикации
    all_recipes = RecipesPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # Создаём Paginator, в который передаём статьи и указываем,
    # что их будет 8 штук на одну страницу
    current_page = Paginator(all_recipes, 8)

    page = request.GET.get('page')
    try:
        context['recipe_lists'] = current_page.page(page)
    except PageNotAnInteger:
        # Если None, то выбираем первую страницу
        context['recipe_lists'] = current_page.page(1)
    except EmptyPage:
        # Если вышли за последнюю страницу, то возвращаем последнюю
        context['recipe_lists'] = current_page.page(current_page.num_pages)
    return render_to_response('mainPage/recipes_list.html', context)


def recipes_detail(request, pk):
    return HttpResponse("OK")