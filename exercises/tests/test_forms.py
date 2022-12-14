from django.forms.models import ModelFormMetaclass
from exercises.forms import MovieForm


def test_create_movie_form_5():
    assert type(MovieForm) == ModelFormMetaclass
    form = MovieForm({"name": "Movie name"})
    form.is_valid()
