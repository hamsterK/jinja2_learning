from jinja2 import Environment, FileSystemLoader

subjects = ["Math", "Physics", "Computer science", "Russian"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.htm')

output = template.render(list_table = subjects)
print(output)
