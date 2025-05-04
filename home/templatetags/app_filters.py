from django import template
import math

register = template.Library()

@register.filter(name="calcnutperc")
def calcnutperc(qty, targetQty):
    actual = float(qty)
    target = float(targetQty)
    return math.ceil(((actual/target) * 100))