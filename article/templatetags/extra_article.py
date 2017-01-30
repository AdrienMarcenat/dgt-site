from django import template
from django.urls import reverse
import markdown

register = template.Library()

@register.filter
def markdownify(text):
    return markdown.markdown(text, safe_mode="escape")
