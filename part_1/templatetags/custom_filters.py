from django import template

register = template.Library()

@register.filter
def clean_float(value):
    try:
        if value is None or value == "":
            return "N/A"
        return str(float(value)).rstrip('0').rstrip('.') if '.' in str(value) else str(value)
    except (ValueError, TypeError):
        return "N/A"