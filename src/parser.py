import json
import re

class Parser(object):
    filepath = None
    text = None

    def __init__(self, file):
        self.filepath = file

    def read_file(self):
        f_stream = open(self.filepath, 'r')
        self.text = f_stream.read()

    def parse_file(self):
        print type(self.text)

        vals = re.findall(r'(\b\d{3}) \S+=(\d+\b)', self.text)
        # print vals, '\n'
        packed = {}
        for each in vals:
            packed[each[0]] = each[1]
        jsoned = json.dumps(packed)
        return jsoned