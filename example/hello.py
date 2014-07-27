import os
from datetime import datetime
import pytz
from pyramid.config import Configurator
from pyramid.view import view_config
from rebecca.bootstraplayout.resources import (
    PageContext,
    BreadCrumb,
    BreadCrumbItem,
)
from rebecca.bootstraplayout.constants import (
    message,
)


here = os.path.dirname(__file__)
JST = pytz.timezone("Japan")
UTC = pytz.utc


@view_config(renderer="index.mako", layout="main")
def greeting(request):
    utcnow = UTC.localize(datetime.utcnow())
    tz = pytz.timezone(pytz.country_timezones("JP")[0])
    now = utcnow.astimezone(tz)
    return dict(message=request.localizer.translate(message),
                now=now, utcnow=utcnow)


def main(global_conf, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_mako")
    config.include("rebecca.bootstraplayout")
    page = PageContext(
            title='this is rebecca.bootstrap demo',
            breadcrumb=BreadCrumb(
                items=[
                    BreadCrumbItem(label='HOME', url="#"),
                    BreadCrumbItem(label='Library', url="#"),
                    BreadCrumbItem(label='Data', active=True),
                    ]
                ),
            )
    config.set_default_page_context(page)
    config.scan(".")
    return config.make_wsgi_app()

if __name__ == '__main__':
    settings = {
        "pyramid.default_locale_name": "ja",
    }
    app = main({}, **settings)
    import waitress
    waitress.serve(app, host='0.0.0.0', port=5000)
