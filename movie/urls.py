from django.conf.urls import patterns, url
from movie import views

urlpatterns = patterns('',
    # ex: /movies/
    url(r'^$', views.index, name='index'),
    # ex: /movies/movies/
    url(r'^movies/$', views.movies, name='movies'),
    # ex: /movies/tvshows/
    url(r'^tvshows/$', views.tvshows, name='tvshows'),
	# ex: /movies/movies/5/
    url(r'^movies/(?P<movie_id>\d+)/$', views.moviedetail, name='moviedetail'),
	# ex: /movies/tvshows/5/
	url(r'^tvshows/(?P<show_id>\d+)/$', views.tvdetail, name='tvdetail'),
	# ex: /movies/tvshows/season/1/
	url(r'^tvshows/season/(?P<season_id>\d+)/$', views.seasondetail, name='seasondetail'),
	# ex: /movies/tvshows/season/episode/1/
	url(r'^tvshows/season/episode/(?P<episode_id>\d+)/$', views.episode, name='episode'),
	url(r'^add/episode/(?P<season_id>\d+)/$', views.addepisode, name='addepisode'),
	url(r'^add/movie/$', views.addmovie, name='addmovie'),
)