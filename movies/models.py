from django.db import models

class Video(models.Model):
    GENRE_CHOICES = [
        ("Comedy", "Comedy"),
        ("Romance", "Romance"),
        ("Action", "Action"),
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Sci-Fi", "Sci-Fi"),
    ]

    movie_id = models.CharField(max_length=20, unique=True)        # MovieID
    title = models.CharField(max_length=200)                       # MovieTitle
    actor1_name = models.CharField(max_length=100)                 # Actor1Name
    actor2_name = models.CharField(max_length=100, blank=True)     # Actor2Name
    director_name = models.CharField(max_length=100)               # DirectorName
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES) # MovieGenre
    release_year = models.PositiveIntegerField()                   # ReleaseYear

    def __str__(self):
        return f"{self.movie_id} - {self.title}"
