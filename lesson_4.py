from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Kolia", "old": 28, "weight": 82.3},
    {"name": "Ivan", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.htm')
msg = tm.render(users=persons)

print(msg)


def loadTpl(path):
    if path == "index":
        return '''Name {{u.name}}, age {{u.old}}'''
    else:
        return '''Data: {{u}}'''


file_loader2 = FunctionLoader(loadTpl)
env2 = Environment(loader=file_loader2)

# tm2 = env2.get_template('index')
tm2 = env2.get_template('index2')
msg2 = tm2.render(u=persons[0])

print(msg2)
