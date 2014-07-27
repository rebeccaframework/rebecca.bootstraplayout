from .interfaces import IPageContext


def includeme(config):
    config.include("pyramid_layout")

    config.add_directive('set_default_page_context',
                         set_default_page_context)
    config.add_request_method('.api.get_default_page_context',
                              "default_page_context",
                              property=True, reify=True)
    config.add_request_method('.api.get_page_context')
    config.add_translation_dirs("rebecca.bootstraplayout:locale/")

    config.scan(".layouts")
    config.scan(".panels")
    config.scan(".subscribers")
    config.add_static_view("bootstrap-static", "static")


def set_default_page_context(config, page_context):
    reg = config.registry
    def register():
        reg.registerUtility(page_context, IPageContext)

    config.action('rebecca.bootstraoplayout.default_page_context', register)
