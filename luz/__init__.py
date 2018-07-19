import click
from huepy import yellow, red

def horizontal():
    ''' prints a horizontal line separator '''
    return(click.echo(yellow('----------------------')))

