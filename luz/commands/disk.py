from __future__ import absolute_import
import os
import json
import click
import ast
import sys
from huepy import yellow, red, white
from luz import horizontal
from click import style as color
# to do: 
# windows OS
# JSON return option


def get_dir_size(json_flag, verbose, path='/'):
    ''' get disk size of directory or file '''

    # check if dir or file exists
    if not os.path.exists(path):
        click.echo(color('provided directory or file does not exist: {}'.format(path), fg='red', bold=True))
        return 'error'
    
    total_size = 0

    # JSON payload
    payload = {}
    payload['total'] = {}
    payload['dirs'] = {}

    # check Directory size if path is Directory
    if os.path.isdir(path) is True:
        for dirpath, dirnames, filenames in os.walk(path):
            dirsize = 0
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    size = os.path.getsize(fp)
                except OSError:
                    pass

                dirsize += size
                total_size += size
                payload['dirs'][fp] = dirsize
    
    # check File size if path is File
    if os.path.isfile(path) is True:
        return click.echo(color(str(os.path.getsize(path)), fg='white'))

    # set total size for b, kb, mb, gb

#    kb = "{0}".format(total_size, ",")
    # payload['total']['b'] = '{:,}'.format(total_size)
    # payload['total']['kb'] = '{:,}'.format(total_size/1000, ",")
    # payload['total']['mb'] = '{:,}'.format(total_size/1000000, ",")
    # payload['total']['gb'] = '{:,}'.format(total_size/1000000000, ",")
    #print(type(payload['total']))
    payload['total']['b'] = total_size
    payload['total']['kb'] = total_size/1000
    payload['total']['mb'] = total_size/1000000
    payload['total']['gb'] = total_size/1000000000

   # print(payload)
    # return total payload data
    return payload


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

    if payload == 'error':
        return

    if json:
        if True in verbose:
            click.echo(color(payload, bg='black', fg='white'))
        else:
            try:
                #payload = ast.literal_eval(json.dumps(payload))
                print(payload)
                click.echo(yellow(json.dump(payload['total'])))
            except AttributeError as e:
                click.echo(red('error generating json, %s' % str(e)))
                click.echo(yellow('total (kb):  ' + str(payload['total']['kb'])))
    else:
        if True in verbose:
            for d in payload['dirs']:
                try:

                    click.echo(color(str(d), fg='yellow') + color('  {:,} bytes'.format(payload['dirs'][d]), fg='white')) 
                    #click.echo(white('{:,} bytes'.format(payload['dirs'][d])))
                    #click.echo(yellow(str(d) + ':  ' + str(payload['dirs'][d]) + ' b'))
                except UnicodeEncodeError as e:
                    click.echo(red('error displaying sub directories %s' % str(e)))

            #click.echo(yellow('total (b):  ' + str(payload['total']['b'])))
            #click.echo(yellow('total (kb):  ' + str(payload['total']['kb'])))
           # click.echo(yellow('total (mb):  ' + str(payload['total']['mb'])))
            #click.echo(yellow('total (gb):  ' + str(payload['total']['gb'])))
        else:
            total_b = str(payload['total']['b'])
            total_kb = str(payload['total']['kb'])
            total_mb = str(payload['total']['mb'])
            total_gb = str(payload['total']['gb'])
            click.echo(yellow("disk space: {0}").format(path))
            horizontal()
            click.echo(white("{0} B\n{1} KB\n{2} MB\n{3} GB\n".format(total_b, total_kb, total_mb, total_gb)))
            
            
            # byte: {1}\nkb: {2}".format(
            #     path, 
            #     total_b, 
            #     total_kb
            # )))


        
    
    #click.echo(yellow(get_dir_size(json, verbose, path)))

disk.add_command(size)