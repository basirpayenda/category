
def single_slug(request, single_slug):
    matching_series = TutorialSeries.objects.filter(
        series_maincategory__category_slug=single_slug)
    # matching_series = TutorialSeries.objects.filter('front-end')
    # matching_series => HTML, CSS, JS & JQuery

    series_urls = {}
    for i in matching_series.all():  # HTML, CSS, JS & JQuery
        part_one = Tutorial.objects.filter(
            tutorial_series__series_title=i.series_title).earliest('tutorial_published')
        series_urls[i] = part_one.tutorial_slug

    return render(request, 'tutorial/sub-category.html', context={
        "tutorial_series": matching_series,
        'part_ones': series_urls
    })
