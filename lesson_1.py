from jinja2 import Template

name = 'Fedor'
age = 28

tm = Template("Hello {{ name.upper() }}")
msg = tm.render(name=name)

print(msg)

tm2 = Template("I am {{ a+2 }} years old and my name is {{ n }}.")
msg2 = tm2.render(n=name, a=age)

print(msg2)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


per = Person("Ania", 18)

# tm3 = Template("I am {{ p.age }} years old and my name is {{ p.name }}.")
tm3 = Template("I am {{ p.get_age() }} years old and my name is {{ p.get_name() }}.")
msg3 = tm3.render(p=per)

print(msg3)

person_d = {"name": "Max", "age": 34}

tm4 = Template("I am {{ p.age }} years old and my name is {{ p.name }}.")  # or p["age"]
msg4 = tm4.render(p=person_d)

print(msg4)
