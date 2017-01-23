#!/usr/bin/env python
import sys
from src.parser import Parser

#run this file from your console, previously switched to the project root
# and set the path to the log-file, which you want to parse
#Sample: "python main.py log.log"
if __name__ == "__main__":
    file_r = sys.argv[1]

    p = Parser(file_r)
    p.read_file()
    jsoned = p.parse_file()
    print jsoned