from django.contrib import admin
from movie.models import Movie, TvShow, Season, Episode

admin.site.register(Movie)
admin.site.register(TvShow)
admin.site.register(Season)
admin.site.register(Episode)
