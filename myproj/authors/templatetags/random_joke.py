from random import choice

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

jokes = [
    'My dog used to chase people on a bike a lot. It got so bad, finally I had to',
    '- Anton, do you think I\'m a bad mother?<br> - My name is Paul.',
    'Can I kangaroo jump higher than a house?<br> Of course, a house doesn\'t jump',
]

@register.simple_tag
def joke(index=None):
    if index is None or not isinstance(index, int) or index >= len(jokes):
        a_joke = choice(jokes)
    else:
        a_joke = jokes[index]
    return mark_safe(f'<p>{a_joke}</p>')
