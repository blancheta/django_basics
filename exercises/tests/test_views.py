class TestExerciseFunctionBasedViews:

    def test_display_hello_word_string_response_1(self, client):
        # Create a django view called `display_hello_view` which returns "Hello world!"
        # Route: /exercises/hello_world
        response = client.get("/exercises/hello_world_str")

        assert response.status_code == 200
        assert response.text == b"Hello world!"
        assert response.headers["Content-Type"] == "plain/text"

    def test_display_hello_username_string_response_2(self, client):
        # Create a django view called `display_hello_username_view`
        # and returns "Hello <username>" in a string response
        # Route: /exercises/hello_username/<username>

        response = client.get("/exercises/func/hello_username_str/me")

        assert response.status_code == 200
        assert response.text == b"Hello me"
        assert response.headers["Content-Type"] == "plain/text"

    def test_display_hello_word_in_template_response_3(self, client):
        # Create a django view called `display_hello_word_in_template`
        # and returns "hello word" in a html response (template)
        # Route: /exercises/hello_word_template
        response = client.get("/exercises/func/hello_world_template/me")

        assert response.status_code == 200
        assert response.text == b"hello world"
        assert response.headers["Content-Type"] == "text/html"

    def test_display_hello_username_in_template_response_4(self, client):
        # Create a django view called `display_hello_username_in_template`
        # and returns "hello word" in a html response (template)
        # Route: /exercises/hello_username_template/<username>
        response = client.get("/exercises/func/hello_username_template/me")

        assert response.status_code == 200
        assert response.text == b"hello me"
        assert response.headers["Content-Type"] == "text/html"

    def test_create_movie_view_6(self, client):
        # Create a view to create a movie from a form url:/movies/create
        response = client.get("/exercises/func/movies/create")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/html"

    def test_edit_movie_view_7(self, client):
        # Create a view to edit a movie from a form url:/movies/edit
        response = client.get("/exercises/func/movies/1/edit")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/html"

    def test_delete_movie_view_8(self, client):
        # Create a view to delete a movie from a form url:/movies/delete
        response = client.get("/exercises/func/movies/1/delete")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/html"


class TestExerciseClassBasedViews:

    def test_display_hello_word_string_response_9(self, client):
        # Create a django view called `display_hello_view` which returns "Hello world!"
        # Route: /exercises/hello_world
        response = client.get("/exercises/hello_world_str")

        assert response.status_code == 200
        assert response.text == b"Hello world!"
        assert response.headers["Content-Type"] == "plain/text"

    def test_display_hello_username_string_response_10(self, client):
        # Create a django view called `display_hello_username_view`
        # and returns "Hello <username>" in a string response
        # Route: /exercises/hello_username/<username>

        response = client.get("/exercises/func/hello_username_str/me")

        assert response.status_code == 200
        assert response.text == b"Hello me"
        assert response.headers["Content-Type"] == "plain/text"

    def test_display_hello_word_in_template_response_11(self, client):
        # Create a django view called `display_hello_word_in_template`
        # and returns "hello word" in a html response (template)
        # Route: /exercises/hello_word_template
        response = client.get("/exercises/func/hello_world_template/me")

        assert response.status_code == 200
        assert response.text == b"hello world"
        assert response.headers["Content-Type"] == "text/html"

    def test_display_hello_username_in_template_response_12(self, client):
        # Create a django view called `display_hello_username_in_template`
        # and returns "hello word" in a html response (template)
        # Route: /exercises/hello_username_template/<username>
        response = client.get("/exercises/class/hello_username_template/me")

        assert response.status_code == 200
        assert response.text == b"hello me"
        assert response.headers["Content-Type"] == "text/html"

    def test_create_movie_view_13(self, client):
        # Create a view to create a movie from a form url:/movies/create
        response = client.get("/exercises/class/movies/create")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/html"

    def test_edit_movie_view_14(self, client):
        # Create a view to edit a movie from a form url:/movies/edit
        response = client.get("/exercises/class/movies/1/edit")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/html"

    def test_delete_movie_view_15(self, client):
        # Create a view to delete a movie from a form url:/movies/delete
        response = client.get("/exercises/class/movies/1/delete")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/html"
