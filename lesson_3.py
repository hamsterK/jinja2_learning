from jinja2 import Template

cars = [
    {'model': 'audi', 'price': 23000},
    {'model': 'skoda', 'price': 17300},
    {'model': 'volvo', 'price': 44300},
    {'model': 'volksvagen', 'price': 21300}
]

tpl = "Total price of cars is {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)
