from django.template.defaulttags import register
from django import template

# register = template.Library()


@register.filter(name='get_value_from_dict')
def get_value_from_dict(dictionary, key):
    return dictionary.get(key)


register.filter('get_value_from_dict', get_value_from_dict)