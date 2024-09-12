#!/usr/bin/python3
import sys
import re

true = 1
false = 0

def lex(file):
    output = []
    in_comment = false
    in_multiline_comment = false
    may_be_in_comment = false
    may_be_out_of_multiline_comment = false
    


    return output

def parse(file):
    return file
if __name__ == "__main__":
    if sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as file:
            if sys.argv[3] == "-o":
                with open(sys.argv[4], "w") as output:
                    output.write(parse(lex(file.readlines())))
