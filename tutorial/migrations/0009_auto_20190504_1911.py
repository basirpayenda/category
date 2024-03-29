# Generated by Django 2.2.1 on 2019-05-04 14:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0008_auto_20190504_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 19, 11, 14, 257986), verbose_name='date Published'),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=150)),
                ('section_content', models.TextField()),
                ('section_published', models.DateTimeField(default=datetime.datetime(2019, 5, 4, 19, 11, 14, 257986), verbose_name='date Published')),
                ('section_slug', models.SlugField(blank=True, default=1)),
                ('section_tutorial', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='tutorial.TutorialSeries')),
            ],
            options={
                'verbose_name_plural': 'Sections',
            },
        ),
    ]
