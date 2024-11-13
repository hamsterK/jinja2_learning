from jinja2 import Environment, FileSystemLoader

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
