import click
import sh
from sh import ErrorReturnCode
from huepy import *
# to do: 
# windows OS
# JSON return option

def get_disk_space(path, json_flag):
    try:
        # if json_flag:
        #     import pprint
        #     return pprint.pprint({'path': path, 'space': sh.du('-sh', path)})
        
        return sh.du('-sh', path)
        
    except ErrorReturnCode as e:
        return e.stdout



@click.group()
def disk():
    ''' 
    Disk space and Partition information 
    '''
    pass

@click.command()
@click.argument('path', default=None)
@click.option('--json', is_flag=True)
def size(path, json=None):
    '''
    check size of a given path or directory
    
    examples: \n\n
        
    luz disk size /tmp \n
        
    luz disk size /home --json (print output in JSON)
    '''
    click.echo('\n'+cyan('%s disk size\n' % path))
    click.echo(yellow(get_disk_space(path, json)))

disk.add_command(size)