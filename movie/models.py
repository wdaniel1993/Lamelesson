from django.db import models
import datetime
import subprocess
from django.utils import timezone
import threading
import base64
import os

downloadpath = "/home/pi/lamelesson"

class Movie(models.Model):
	name = models.CharField(max_length=200)
	destinationfile = models.CharField(max_length=200)
	sourcefile = models.CharField(max_length=200)
	download_begin_date = models.DateTimeField('download started', null=True)
	download_success_date = models.DateTimeField('download finished', null=True)
	
	def __unicode__(self):
	       	return self.name

	def download_file(self):
		thread = Downloader(self)
		thread.start()
		
	def size(self):
		try:
			path = "".join((downloadpath+self.destinationfile).split())
			size = os.stat(path).st_size / (2**20)
			return str(size) + " MB"
		except:
			return "0 MB"

class TvShow(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name
			
class Season(models.Model):
	show = models.ForeignKey(TvShow)
	nr = models.IntegerField(max_length=5, null=True, blank=True)
	
	def __unicode__(self):
		return self.show.name + " S" + unicode(self.nr)
			
class Episode(models.Model):
	season = models.ForeignKey(Season)
	nr = models.IntegerField(max_length=5, null=True, blank=True)
	destinationfile = models.CharField(max_length=200)
	sourcefile = models.CharField(max_length=200)
	download_begin_date = models.DateTimeField('download started', null=True)
	download_success_date = models.DateTimeField('download finished', null=True)

	def __unicode__(self):
		return self.season.show.name + " S" + unicode(self.season.nr) + " E" + unicode(self.nr)
			
	def download_file(self):
		thread = Downloader(self)
		thread.start()
		
	def size(self):
		try:
			path = "".join((downloadpath+self.destinationfile).split())
			size = os.stat(path).st_size / (2**20)
			return str(size) + " MB"
		except:
			return "0 MB"

class Downloader(threading.Thread): 
	def __init__(self, movie):
		threading.Thread.__init__(self) 
		self.movie = movie
	
	def run(self):
		name = unicode(self.movie)
		viewpath = "/static/movies/"
		self.movie.download_begin_date = datetime.datetime.now()
		self.movie.destinationfile = os.path.join(viewpath,"".join((unicode(self.movie)+".mp4").split()))
		path = "".join((downloadpath+self.movie.destinationfile).split())
		self.movie.save()
		returncode = subprocess.call(['wget',self.movie.sourcefile,'-O',path])
		
		if returncode == 0:
			self.movie.download_success_date = datetime.datetime.now()
		else:
			self.movie.destinationfile = 'ERROR'
		self.movie.save()