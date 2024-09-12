#!/usr/bin/python3
import sys
import re

true = 1
false = 0

commands = {
    0: "comment",
    1: "function_usage",
    2: "function_definition",
}

def lex(file):
    output = []
    in_comment = false
    in_multiline_comment = false
    may_be_in_comment = false
    may_be_out_of_multiline_comment = false

    for line in file:
        append = []
        if line[:2] == "//":
            append.append(0)
            append.append(line[2:])
        output.append(append)


    return output

def parse(file):
    output = ""
    for line in file:
        if len(line) > 0:
            match line[0]:
                case 0:
                    output += ";"
                    output += line[1]
            
    return output
if __name__ == "__main__":
    if sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as file:
            if sys.argv[3] == "-o":
                with open(sys.argv[4], "w") as output:
                    output.write(parse(lex(file.readlines())))
