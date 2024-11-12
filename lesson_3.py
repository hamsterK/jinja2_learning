from jinja2 import Template

cars = [
    {'model': 'audi', 'price': 23000},
    {'model': 'skoda', 'price': 17300},
    {'model': 'volvo', 'price': 44300},
    {'model': 'volksvagen', 'price': 21300}
]

# tpl = "Total price of cars is {{ cs | sum(attribute='price') }}"
# tpl = "The most expensive car is {{ (cs | max(attribute='price')).model }}"
# tpl = "Car: {{ cs | random }}"
tpl = "Car: {{ cs | replace('o', 'O') }}"


tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Kolia", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.0}
]

tpl2 = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm2 = Template(tpl2)
msg2 = tm2.render(users=persons)

print(msg2)


html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}    
'''

tm3 = Template(html)
msg3 = tm3.render()

print(msg3)


# call - built-in macros
persons2 = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Kolia", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.0}
]

html2 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}    
'''

tm4 = Template(html2)
msg4 = tm4.render(users=persons2)

print(msg4)
