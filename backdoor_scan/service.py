from lib import *
import os
import re

class service():
    service_dir_list = ["/etc/systemd/system"]

    def detect(self, image):
        results = []

        for service_dir in self.service_dir_list:
            for root, dirs, files in image.walk(service_dir):
                for file in files:
                    try:
                        filepath = os.path.join(root, file)
                        f = image.open(filepath, mode="r")
                        f_content = f.read()
                        for backdoor_regex in regex.backdoor_regex_list:
                            if re.search(backdoor_regex, f_content):
                                r = result.Result()
                                r.image_id = image.id()
                                if len(image.reporefs()) > 0:
                                    r.image_ref = image.reporefs()[0]
                                else:
                                    r.image_ref = image.id()
                                r.filepath = filepath
                                r.description = "regex: " + backdoor_regex
                                results.append(r)
                    except FileNotFoundError:
                        continue
                    except BaseException as e:
                        logger.logger.error(e)
        return results