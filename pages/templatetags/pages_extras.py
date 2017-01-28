from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.simple_tag
def navactiveWord(request, word):
    if word in request.path:
        return "active"
    return ""
 
@register.simple_tag
def url_tag(request, word):
    if word in request.path:
        return "active"
    return ""
