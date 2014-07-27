from zope.interface import implementer
from .interfaces import (
    IPageContext,
    IBreadCrumb,
    IBreadCrumbItem,
)


@implementer(IPageContext)
class PageContext(object):
    def __init__(self, title=None, breadcrumb=None):
        self.title = title
        self.breadcrumb = breadcrumb


@implementer(IBreadCrumb)
class BreadCrumb(object):
    def __init__(self, items):
        self.items = items


@implementer(IBreadCrumbItem)
class BreadCrumbItem(object):
    def __init__(self, url=None, label=None, active=False):
        self.url = url
        self.label = label
        self.active = active
