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
    global image_ids
    image_ids.append(image.id())
    if len(image.reporefs()) > 0:
        log.info("start scan: " + image.reporefs()[0])
    else:
        log.info("start scan: " + image.id())

@cli.resultcallback()
def callback(format):
    pass

if __name__ == '__main__':
    cli()
