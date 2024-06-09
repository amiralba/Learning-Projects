import time
import click
import asyncio
from utils import Circle

@click.group()
def cli():
    pass

@click.command()
def circle():
    _circle = Circle(5)
    for i in range(30):
        click.clear()
        for i in range(i):
            print()
        _circle.draw()
        # asyncio.sleep(0.1)
        time.sleep(0.1)

cli.add_command(circle)

if __name__ == "__main__":
    cli()