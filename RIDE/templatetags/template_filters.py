from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def make_table(stations):
    res = ''
    for key in stations['Arrives'].keys():
        res += '<tr>'
        for value in stations:
            res = res + '<td>' + str(stations[value][key]) + '</td>'
        res += '</tr>'

    return mark_safe(res)


@register.simple_tag
def make_fare_table(fares):
    res = '<thead><tr>'
    for i in range(0, 4):
        if i == 0:
            res += '<th>Type</th>'
        else:
            res += '<th>' + str(fares[str(i)]['0']) + '</th>'
    res += '</tr></thead><tbody>'
    for i in range(1, 7):
        res += '<tr>'
        for j in range(0, 4):
            res = res + '<td>' + str(fares[str(j)][str(i)]) + '</td>'
        res += '</tr>'
    res += '<tbody>'

    return mark_safe(res)
