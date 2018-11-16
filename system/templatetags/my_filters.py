from django import template

register = template.Library()


@register.inclusion_tag('block/navbar.html')
def show_navbar(section):
    return {'section': section}


@register.filter
def ellipsize(text, n):
    if len(text) > n:
        return text[:n] + ".."
    return text


@register.filter
def multiply(number, number2):
    return number * number2


@register.filter
def subtract(number, number2):
    return number - number2


@register.filter
def divide(number, number2):
    if number2 == 0.0:
        return 0.0
    return number / number2
