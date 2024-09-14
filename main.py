#!/usr/bin/python3
import sys
import re

true = 1
false = 0

commands = {
        "comment": 0,
        "function_usage": 1,
        "function_definition": 2,
        "if_statement": 3,
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
            append.append(commands["comment"])
            append.append(line[2:])
        elif line[:2] == "/*":
            in_multiline_comment = true
        elif line[:-2] == "*/":
            in_multiline_comment = false
        if in_multiline_comment:
            if line[:2] == "/*":
                append.append(commands["comment"])
                append.append(line[2:])
            else:
                if line[:2] != "*/":
                    append.append(commands["comment"])
                    append.append(line)
            
        if len(append) > 0:
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
    try:
        if sys.argv[1] == "-i" or sys.argv[1] == "--input":
            with open(sys.argv[2], "r") as file:
                if sys.argv[3] == "-o" or sys.argv[3] == "--output":
                    with open(sys.argv[4], "w") as output:
                        output.write(parse(lex(file.readlines())))
    except IndexError:
        print("usage: " + sys.argv[0] + " [-i <input file>] [-o <output file>]\n\noptions:\n  -i, --input             specifies the input file\n  -o, --output            specifies the output file")
