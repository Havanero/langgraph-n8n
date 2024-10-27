from jinja2 import Environment, FileSystemLoader


def load_prompt(context):
    env = Environment(loader=FileSystemLoader("templates"))

    template = env.get_template("rag_template.txt")

    result = template.render(context=context)
    return result
