import click

from app.workflow import app


@click.group()
def cli():
    pass


@cli.command()
@click.option("-msg", "--msg", default="hello there", type=str)
@click.argument("msg")
def run(msg: str):
    """run agent"""
    input_ = {"messages": [("user", msg)]}
    print("started", msg)
    for evt in app.stream(input_, {}, stream_mode="values"):
        print(evt["messages"][-1].pretty_print())
