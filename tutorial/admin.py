from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.db import models
from tinymce.widgets import TinyMCE


class TutorialAdmin(admin.ModelAdmin):
    # fields = [
    #     'tutorial_title',
    #     'date_published',
    #     'tutorial_content'
    # ]
    fieldsets = [
        ('Tutorial Title/ Date', {'fields': [
            'tutorial_title', 'tutorial_published']}
         ), (
            'Content', {'fields': ['tutorial_content',
                                   'tutorial_series', 'tutorial_slug']}
        )
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class TutorialCategoryAdmin(admin.ModelAdmin):
    fields = [
        'category_title',
        'category_summary'
    ]


class TutorialSeriesAdmin(admin.ModelAdmin):
    fields = [
        'series_title',
        'series_maincategory',
        'series_summary',
        'series_slug'
    ]


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialCategory, TutorialCategoryAdmin)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)
