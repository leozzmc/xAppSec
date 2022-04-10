from register import register
from lib import log
from lib import result
from lib import regex
import os
import re


@register.register("test")
class test:
    """
    test backdoor testing plugin
    """
    def detect(self, image):
        results = []
        return results
