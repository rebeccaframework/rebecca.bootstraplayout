def includeme(config):
    config.include("pyramid_layout")
    config.scan(".layouts")
    config.scan(".panels")
    config.add_static_view("bootstrap-static", "static")
