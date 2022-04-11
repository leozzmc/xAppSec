#!/usr/bin/env python3
import click
from veinmind import *



image_ids = []

@command.group()
def cli():
    pass

@cli.image_command()
def test(image):
    """Just a test function"""
    global image_ids
    image_ids.append(image.id())
    if len(image.reporefs()) > 0:
        log.info("start scan: " + image.reporefs()[0])
    else:
        log.info("start scan: " + image.id())

@cli.resultcallback()
def callback():
    pass

if __name__ == '__main__':
    cli()
