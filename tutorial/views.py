from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries, Section
from django.contrib.auth.forms import UserCreationForm


def series_view(request, cat_slug):
    matching_series = TutorialSeries.objects.filter(series_maincategory__category_slug=cat_slug)  

    return render(request, 'tutorial/sub-category.html', context={
        "matching_series": matching_series,
    })


def tutorial_view(request, cat_slug, series_slug):
    matching_series = Tutorial.objects.filter(tutorial_series__series_slug=series_slug)  

    return render(request, 'tutorial/sub-sub-category.html', context={
        "matching_series": matching_series,
    })


def tutorial_details_view(request, cat_slug, series_slug, tutorial_slug):

    object = get_object_or_404(Tutorial, tutorial_slug=tutorial_slug)
    return render(request, 'tutorial/tutorial-detail.html', context={
        'obj': object
    })


def home_page(request):
    return render(request=request, template_name='tutorial/home.html', context={'tutorials': TutorialCategory.objects.all()})


def tutorial_detail(request, id):
    return render(request, template_name='tutorial/tutorial_detail.html', context={'obj': Tutorial.objects.get(id=id)})
