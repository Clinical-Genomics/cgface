import click
import yaml
from .api import CgFace

@click.group()
@click.option('-c', '--config', type=click.File('r'))
@click.pass_context
def cgface(context, config):
    """interface with cg!"""
    context.obj = yaml.load(config) if config else {}

@cgface.command()
@click.argument('tag_name')
@click.argument('key', required=False)
@click.pass_context
def apptag(context, tag_name, key):
    """get apptag information from cg"""
    cgface_obj = CgFace(url=context.obj['url'])
    click.echo(cgface_obj.apptag(tag_name=tag_name, key=key))
