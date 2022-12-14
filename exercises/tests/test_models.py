import pytest
from exercises.models import Movie


@pytest.mark.django_db
def test_create_model_movie_5(self):
  # Create a model called "Movie" and containing an id, a name
  movie = Movie(name="Star Wars - The Phantom Menace")
  assert movie.name == "Star Wars - The Phantom Menace"
