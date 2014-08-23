from zope.interface import Interface, Attribute


class IPageContext(Interface):
    title = Attribute(u"title for page")


class IBreadCrumb(Interface):
    items = Attribute(u"list for bread crumb items")


class INavigationList(Interface):
    items = Attribute(u"list for link")


class ILinkItem(Interface):
    url = Attribute(u"url for item")
    label = Attribute(u"label for item")
    active = Attribute(u"representation for item state")


class IPanel(Interface):
    heading = Attribute(u"heading for panel")
    footer = Attribute(u"footer for panel")
    body = Attribute(u"contents for panel")
