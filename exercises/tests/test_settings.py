from django.conf import settings


class TestExerciseFunctionBasedViews:

    def test_exercises_app_added_0(self):
        assert "exercises" in settings.INSTALLED_APPS
