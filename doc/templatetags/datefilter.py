from django import template
from django.utils.dateformat import dateformat

import datetime


register = template.Library()

@register.filter
def datefilter():
    d = datetime.datetime.now()
    df = dateformat(d)
    print(df.format('jS F Y H:i'))