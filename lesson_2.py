from jinja2 import Template
from markupsafe import escape


data = """{% raw %}Module jinja inputs correct value
instead of {{ name }}{% endraw %}"""

tm = Template(data)
msg = tm.render(name="Fedor")

print(msg)

link = '''In html document links are defined as follows:
<a href="#">Link</a>'''

tm2 = Template("{{ link | e}}")  # e to shield special symbols < > " '
msg2 = tm2.render(link=link)

print(msg2)

# same with escape imported from jinja2

link2 = '''In html document links are defined as follows:
<a href="#">Link</a>'''

msg3 = escape(link2)
print(msg3)
print()


cities = [{'id': 1, 'city': 'Minsk'},
          {'id': 2, 'city': 'Warsaw'},
          {'id': 3, 'city': 'Krakow'}]

# -% to remove redundant empty line
link3 = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}
    {{c['city']}}    
{% endfor -%}
</select>'''

tm = Template(link3)
msg4 = tm.render(cities=cities)

print(msg4)


link4 = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 2 -%}}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Minsk" -%}
    <option>{{c['city'][:1]}}</option>    
{% else -%}
    {{c['city']}}        
{% endif -%}    
{% endfor -%}
</select>'''

tm = Template(link4)
msg5 = tm.render(cities=cities)

print(msg5)
