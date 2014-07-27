import os
from pyramid.config import Configurator
from pyramid.view import view_config


here = os.path.dirname(__file__)


@view_config(renderer="index.mako", layout="base")
def greeting(request):
    return dict(message="Hello")


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_mako")
    config.include("rebecca.bootstraplayout")
    config.scan(".")
    return config.make_wsgi_app()

if __name__ == '__main__':
    app = main({})
    import waitress
    waitress.serve(app, host='0.0.0.0', port=5000)
