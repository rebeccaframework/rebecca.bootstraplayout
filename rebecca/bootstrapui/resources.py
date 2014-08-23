from zope.interface import implementer
from .interfaces import (
    IPageContext,
    IBreadCrumb,
    INavigationList,
    ILinkItem,
    IPanel,
)


@implementer(IPageContext)
class PageContext(object):
    def __init__(self, title=None, breadcrumb=None, sidemenu=None):
        self.title = title
        self.breadcrumb = breadcrumb
        self.sidemenu = sidemenu


@implementer(IBreadCrumb)
class BreadCrumb(object):
    def __init__(self, items):
        self.items = items


@implementer(INavigationList)
class NavigationList(object):
    def __init__(self, items):
        self.items = items


@implementer(ILinkItem)
class LinkItem(object):
    def __init__(self, url=None, label=None, active=False):
        self.url = url
        self.label = label
        self.active = active


@implementer(IPanel)
class Panel(object):
    def __init__(self, contents, heading=None, footer=None):
        self.contents = contents
        self.heading = heading
        self.footer = footer
