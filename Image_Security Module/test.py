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
    print("[1] " + image.id())
    print(image.reporefs())

@cli.resultcallback()
def callback(result):
    pass

if __name__ == '__main__':
    cli()
