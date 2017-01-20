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
        ids = re.findall(r'\b\d{3} ', self.text)
        print len(ids)
        vals = re.findall(r'=\d+', self.text)
        print len(vals)
        packed = {}
        for i, j in enumerate(ids):
            packed[j] = vals[i].replace('=', '')
        print packed