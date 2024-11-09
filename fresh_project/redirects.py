from django.views.generic import RedirectView


class Redirect(RedirectView):
    pattern_name = 'schema-swagger-ui'
    url = '/swagger'
