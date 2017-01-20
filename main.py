#!/usr/bin/env python
import sys
from src.parser import Parser


if __name__ == "__main__":
    file_r = sys.argv[1]

    p = Parser(file_r)
    p.read_file()
    p.parse_file()
