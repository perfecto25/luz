import click
import os
import json
from huepy import *
# to do: 
# windows OS
# JSON return option


def get_dir_size(json_flag, verbose, path='/'):
    
    total_size = 0

    # JSON payload
    payload = {}
    payload['total'] = {}
    payload['dirs'] = {}

    for dirpath, dirnames, filenames in os.walk(path):
        dirsize = 0

        for f in filenames:
            #print f
            fp = os.path.join(dirpath, f)
            try:
                size = os.path.getsize(fp)
            except OSError:
                print('error %s' % f)
                pass
            #print("{0} {1}").format(size, fp)
            #print(dirpath, dirnames, filenames,size)
            dirsize += size
           # print(dirpath)
            total_size += size
            print(fp)
            payload['dirs'][fp] = dirsize
    
    # set total size for b, kb, mb, gb

#    kb = "{0}".format(total_size, ",")
    payload['total']['b'] = '{:,}'.format(total_size)
    payload['total']['kb'] = '{:,}'.format(total_size/1000, ",")
    payload['total']['mb'] = '{:,}'.format(total_size/1000000, ",")
    payload['total']['gb'] = '{:,}'.format(total_size/1000000000, ",")

    # return total payload data
    return dict(payload)


@click.group()
def disk():
    ''' 
    Disk space and Partition information 
    '''
    pass

@click.command()
@click.argument('path', default=None)
@click.option('--json', is_flag=True)
@click.option('--verbose', '-v', multiple=True, is_flag=True, help="print all sub directories and their sizes")
def size(path, json=False, verbose=False):
    '''
    check size of a given path or directory
    
    examples: \n\n
      luz disk size /tmp \n 
      luz disk size /home --json (print output in JSON) \n
      luz disk size /home -v (print names and size of all subfolders)

    '''
    #click.echo('\n'+cyan('%s disk size\n' % path))

    payload = get_dir_size(json, verbose, path)

    if json:
        if True in verbose:
            print type(payload)
            click.echo(yellow(payload))
        else:
            click.echo(yellow(json.dumps(payload['total'])))
    else:
        if True in verbose:
            for d in payload['dirs']:
                click.echo(yellow(str(d) + ':  ' + str(payload['dirs'][d]/1000) + ' kb'))
            click.echo(yellow('total (b):  ' + str(payload['total']['b'])))
            click.echo(yellow('total (kb):  ' + str(payload['total']['kb'])))
            click.echo(yellow('total (mb):  ' + str(payload['total']['mb'])))
            click.echo(yellow('total (gb):  ' + str(payload['total']['gb'])))
        else:
            click.echo(yellow('total:  ' + str(payload['total']['kb']) + ' kb'))

        
    
    #click.echo(yellow(get_dir_size(json, verbose, path)))

disk.add_command(size)