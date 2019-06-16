from django.db import models
from datetime import datetime
from django.utils.text import slugify
from tinymce.widgets import TinyMCE
from django.db import models


class TutorialCategory(models.Model):
    category_title = models.CharField(max_length=150)
    category_summary = models.CharField(max_length=150)
    category_slug = models.SlugField(default=1, blank=True)

    def __str__(self):
        return self.category_title

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_title)
        super(TutorialCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class TutorialSeries(models.Model):
    series_title = models.CharField(max_length=200)
    series_maincategory = models.ForeignKey(
        TutorialCategory, default=1, on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    series_slug = models.SlugField(default=1, blank=True)

    def __str__(self):
        return self.series_title

    class Meta:
        verbose_name_plural = 'Series'


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=150)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        "date Published", default=datetime.now())
    tutorial_series = models.ForeignKey(
        TutorialSeries, default=1, on_delete=models.SET_DEFAULT)
    tutorial_slug = models.SlugField(default=1, blank=True)

    def snippet(self):
        return self.tutorial_content[:200] + '...'

    def __str__(self):
        return self.tutorial_title

    def save(self, *args, **kwargs):
        self.tutorial_slug = slugify(self.tutorial_title)
        super(Tutorial, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tutorials'


class Section(models.Model):
    section_title = models.CharField(max_length=150)
    section_content = models.TextField()
    section_published = models.DateTimeField(
        "date Published", default=datetime.now())
    section_tutorial = models.ForeignKey(
        TutorialSeries, default=1, on_delete=models.SET_DEFAULT)
    section_slug = models.SlugField(default=1, blank=True)

    def snippet(self):
        return self.section_content[:200] + '...'

    def __str__(self):
        return self.section_title

    def save(self, *args, **kwargs):
        self.section_slug = slugify(self.section_title)
        super(Section, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Sections'
