from django import template


from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='domain')
@stringfilter
def cut_email_domain(value):
    if '@' not in value:
        return '[email not stated]'
    return value.partition('@')[2]
