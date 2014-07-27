import functools
from webhelpers2.html import HTML, escape, literal
from babel.dates import format_date, format_datetime, format_time
from babel.numbers import format_number, format_decimal, format_percent


def bind_locale(func, localename):
    return functools.partial(func, locale=localename)


class WebHelper(object):
    def __init__(self, request):
        self.request = request
        self.locale_name = request.locale_name
        self.HTML = HTML
        self.escape = escape
        self.literal = literal
        self.format_date = bind_locale(format_date, self.locale_name)
        self.format_datetime = bind_locale(format_datetime, self.locale_name)
        self.format_time = bind_locale(format_time, self.locale_name)
        self.format_number = bind_locale(format_number, self.locale_name)
        self.format_decimal = bind_locale(format_decimal, self.locale_name)
        self.format_percent = bind_locale(format_percent, self.locale_name)
