# Create your views here.
from django.http import HttpResponseRedirect
from movie.models import Movie,TvShow,Season,Episode
from movie.forms import EpisodeForm, MovieForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404



@login_required
def index(request):
    return render(request, 'movie/index.html', None)
	
@login_required
def movies(request):
	movies = get_list_or_404(Movie, download_success_date__isnull = False)
	return render(request, 'movie/movies.html', {'movies':movies})

@login_required
def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/movie.html', {'movie': movie})
	
@login_required
def tvshows(request):
	tvshows = get_list_or_404(TvShow)
	return render(request, 'movie/tvshows.html', {'tvshows':tvshows})
	
@login_required
def tvdetail(request, show_id):
	tvshow = get_object_or_404(TvShow, pk=show_id)
	seasons = tvshow.season_set.all()
	return render(request, 'movie/seasons.html', {'tvshow': tvshow, 'seasons':seasons})
	
@login_required
def episode(request, episode_id):
	episode = get_object_or_404(Episode, pk=episode_id)
	return render(request, 'movie/episode.html', {'episode':episode})
	
@login_required
def seasondetail(request, season_id):
	season = get_object_or_404(Season, pk=season_id)
	episodes = season.episode_set.filter(download_success_date__isnull = False)
	return render(request, 'movie/season.html', {'season': season, 'episodes':episodes})
	
@login_required
def addepisode(request,season_id):
	form = EpisodeForm()
	if request.method == 'POST': # If the form has been submitted...
		form = EpisodeForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			e = Episode()
			e.season = Season.objects.get(pk=season_id)
			e.nr = form.cleaned_data['nr']
			e.sourcefile = form.cleaned_data['url']
			e.save()
			e.download_file()
			return HttpResponseRedirect('/movies/') # Redirect after POST
	
	return render(request, 'movie/addepisode.html', {'form': form})
		
@login_required
def addmovie(request):
	form = MovieForm()
	if request.method == 'POST': # If the form has been submitted...
		form = MovieForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			m = Movie()
			m.name = form.cleaned_data['name']
			m.sourcefile = form.cleaned_data['url']
			m.save()
			m.download_file()
			return HttpResponseRedirect('/movies/') # Redirect after POST<	
	return render(request, 'movie/addmovie.html', {'form': form})