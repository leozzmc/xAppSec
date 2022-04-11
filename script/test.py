#!/usr/bin/env python3
import click
from veinmind import *

image_ids = []
@click.group()
@click.option('--format', default="stdout", help="output format e.g. stdout/json")
def cli(format):
    pass

@cli.command()
def test(image):
    """Just a test function"""
    refs = image.reporefs()
    if len(refs) > 0:
        ref = refs[0]
    else:
        ref = image.id()
    log.info("start scan: " + ref)

@cli.resultcallback()
def callback():
    pass

if __name__ == '__main__':
    cli()
