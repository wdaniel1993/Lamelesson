from django import forms

class EpisodeForm(forms.Form):
	nr = forms.IntegerField()
	url = forms.URLField(label='Download-URL')
	
	
class MovieForm(forms.Form):
	name = forms.CharField(max_length=200)
	url = forms.URLField(label='Download-URL')