from django import template

register = template.Library()
@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adds a CSS class (like 'form-control') to a Django form field in templates.
    Usage in template:
        {{ form.username|add_class:"form-control" }}
    
    """
    return field.as_widget(attrs={"class": css_class})