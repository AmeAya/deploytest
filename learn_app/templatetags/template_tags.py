from django import template

register = template.Library()

@register.filter(name='contentByCategory', safe=True)
def contentByCategory(content, category):
    return content.filter(category=category)
