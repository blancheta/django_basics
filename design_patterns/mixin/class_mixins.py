
class TemplateView:

    def get_context_data(self):
        print("Running get_context_data into TemplateView")
        return {
            "user": "Brian"
        }

    def get_queryset(self):
       return "Get queryset into TemplateView"


# We want to add a recommended post panel on each view visible by the user

class UserDetailsView(TemplateView):

    def get_context_data(self):

        context = super().get_context_data()

        context['user'] = 'Brian'
        context['latest_recommended_post'] = [{
            'id': 0,
            'name': "Become a Pythonista",
            'link': "http://www.example.com"
        }]

        return context

# Hijacking example -------

# So if we want to display the latest recommended post in many views
# it would mean that we need to either change tha parent TemplateView
# or create a Mixin to only overload the get_context_data


class LatestRecommendedPostContextMixin:

    def get_context_data(self):
        print("Running get_context_data into MyDjangoView")

        context = {'user': 'Brian'}

        context['latest_recommended_post'] = [{
            'id': 0,
            'name': "Become a Pythonista",
            'link': "http://www.example.com"
        }]

        return context


# class HomeView(TemplateView):
#     def get_context_data(self):
#         print("Running get_context_data into HomeView")
#
#         context = {'user': 'Brian'}
#         context['latest_recommended_post'] = [{
#             'id': 0,
#             'name': "Become a Pythonista",
#             'link': "http://www.example.com"
#         }]
#
#         return context
#
#
# class AboutView(TemplateView):
#
#     def get_context_data(self):
#         print("Running get_context_data into AboutView")
#
#         context = {'user': 'Brian'}
#         context['latest_recommended_post'] = [{
#             'id': 0,
#             'name': "Become a Pythonista",
#             'link': "http://www.example.com"
#         }]
#
#         return context


class HomeView(LatestRecommendedPostContextMixin, TemplateView):
    pass


class AboutView(LatestRecommendedPostContextMixin, TemplateView):
    pass


class OtherView(TemplateView):
    pass


# Home page
home_page = HomeView()
print(home_page.get_context_data())
print(home_page.get_queryset())

# About page
about_page = AboutView()
print(about_page.get_context_data())
print(about_page.get_queryset())

# Other page
other_page = OtherView()
print(other_page.get_context_data())
print(other_page.get_queryset())
