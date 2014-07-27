from .interfaces import IPageContext


def get_default_page_context(request):
    return request.registry.getUtility(IPageContext)


def get_page_context(request, context):
    reg = request.registry
    adapted_page_context =  reg.queryAdapter(context, IPageContext)
    if adapted_page_context is not None:
        return adapted_page_context
    return get_default_page_context(request)
