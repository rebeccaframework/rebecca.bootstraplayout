from zope.interface import Interface, Attribute


class IPageContext(Interface):
    title = Attribute(u"title for page")
