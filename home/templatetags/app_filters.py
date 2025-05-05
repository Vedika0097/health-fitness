from django import template
import math

register = template.Library()

@register.filter(name="calcnutperc")
def calcnutperc(qty, targetQty):
    actual = float(qty)
    target = float(targetQty)
    val = round(math.ceil(((actual/target) * 100))/5)*5
    return val