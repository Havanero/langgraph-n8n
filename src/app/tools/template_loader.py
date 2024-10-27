from jinja2 import Environment, PackageLoader


def load_prompt(context):
    env = Environment(loader=PackageLoader("app", "templates"))
    template = env.get_template("rag_template.txt")

    result = template.render(context=context)
    return result
