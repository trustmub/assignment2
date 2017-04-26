from pyramid.config import Configurator
from .views import hello_world, index


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    # config.include('pyramid_cameleon')
    # config.add_jinja2_search_path("templates")

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    config.add_route('index', '/index/')
    config.add_view(index, route_name='index')

    config.scan()
    return config.make_wsgi_app()
