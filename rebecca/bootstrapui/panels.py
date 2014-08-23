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


@panel_config(name="navigationlist",
              renderer="templates/panels/navigationlist.mako")
def navigationlist_panel(context, request, navigationlist):
    return dict(navigationlist=navigationlist)


@panel_config(name="panel",
              renderer="templates/panels/panel.mako")
def panel_panel(context, request, panel, panel_style="panel-default"):
    return dict(panel=panel, panel_style=panel_style)
