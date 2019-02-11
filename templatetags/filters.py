from statik.templatetags import register
from collections import defaultdict

@register.filter(name='group_by_year')
def group_by_year(values):
    values_by_year = defaultdict(list)
    for v in values:
        values_by_year[v.date.year].append(v)
    return values_by_year.items()

@register.filter(name='deslugify')
def deslugify(value):
    return ' '.join(value.split('-')).capitalize()
