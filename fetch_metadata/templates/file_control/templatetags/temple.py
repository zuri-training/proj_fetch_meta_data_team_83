import mimetypes 
from django import template
register = template.Library()

@register.filter(name=filetype)
def filetype(value):
    return mimetypes.guess_types(value, strict=True)