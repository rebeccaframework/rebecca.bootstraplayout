from pyramid_layout.panel import panel_config


@panel_config(name="page_header",
              renderer="templates/panels/page_header.mako")
def page_header_panel(context, request):
    page_context = request.get_page_context(context)
    return dict(page_context=page_context)


@panel_config(name="breadcrumb",
              renderer="templates/panels/breadcrumb.mako")
def breadcrumb_panel(conext, request, breadcrumb):
    return dict(breadcrumb=breadcrumb)
