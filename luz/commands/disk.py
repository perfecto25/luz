import click
import psutil

@click.command()
@click.argument('path', default='/')
def disk(path):
    ''' - Disk, Mount and Partition information '''
    disk_percent = psutil.disk_usage(path)[3]
    click.echo(disk_percent)

