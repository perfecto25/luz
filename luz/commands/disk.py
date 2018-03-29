import click
import sh
from sh import ErrorReturnCode
from huepy import *
# to do: 
# windows OS
# JSON return option

def get_disk_space(path):
    try:
        return sh.du('-sh', path)
    except ErrorReturnCode as e:
        return e.stdout


@click.command()
@click.argument('path', default='/')
def disk(path):
    ''' - Disk, Mount and Partition information '''
    click.echo('\n'+cyan('getting disk size for %s\n' % path))
    click.echo(yellow(get_disk_space(path)))

