from pyramid_layout.layout import layout_config


@layout_config(name="base", template="templates/base.mako")
class BaseLayout(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.bootstrap_css = "rebecca.bootstraplayout:static/bootstrap/css/bootstrap.min.css"
        self.jquery = "rebecca.bootstraplayout:static/js/jquery-1.11.1.min.js"
        self.bootstrap_js = "rebecca.bootstraplayout:static/bootstrap/js/bootstrap.min.js"
