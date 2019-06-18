from django.urls import path, reverse
from . import views


app_name = 'tutorial'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('<cat_slug>/', views.series_view, name='single_slug'),
    path('<cat_slug>/<series_slug>/', views.tutorial_view, name='sub_sub_cat'),
    path('<cat_slug>/<series_slug>/<tutorial_slug>/', views.tutorial_details_view, name='tutorial_detail')
]


