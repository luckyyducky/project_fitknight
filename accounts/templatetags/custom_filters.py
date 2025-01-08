from django import template

register = template.Library()

@register.filter
def type_name(value):
    return value.__class__.__name__
