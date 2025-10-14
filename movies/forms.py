from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            "movie_id", "title", "actor1_name", "actor2_name",
            "director_name", "genre", "release_year",
        ]
        widgets = {
            "movie_id": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "actor1_name": forms.TextInput(attrs={"class": "form-control"}),
            "actor2_name": forms.TextInput(attrs={"class": "form-control"}),
            "director_name": forms.TextInput(attrs={"class": "form-control"}),
            "genre": forms.Select(attrs={"class": "form-select"}),
            "release_year": forms.NumberInput(attrs={"class": "form-control", "min": 1888, "max": 2100}),
        }
