from django import template
import math

register = template.Library()


@register.filter
def time_formatter(time):
    time = int(time)
    _min = math.floor((time % 3600) / 60)
    _sec = math.floor(time % 60)

    if _sec < 10:
        sec = f"0{_sec}"

    return f"{_min}:{_sec}"
