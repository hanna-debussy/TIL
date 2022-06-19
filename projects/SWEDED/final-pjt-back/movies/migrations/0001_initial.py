# Generated by Django 3.2.12 on 2022-05-20 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('ovierview', models.TextField()),
                ('release_date', models.CharField(max_length=50)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('poster_path', models.CharField(max_length=500)),
                ('runtime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GetRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('short_comment', models.CharField(max_length=200)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
