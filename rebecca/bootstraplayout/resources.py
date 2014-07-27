from zope.interface import implementer
from .interfaces import IPageContext


@implementer(IPageContext)
class PageContext(object):
    def __init__(self, title=None):
        self.title = title
