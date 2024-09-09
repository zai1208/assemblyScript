#!/usr/bin/python3
import sys

true = 1
false = 0

def lex(file):
    output = []
    in_comment = false
    in_multiline_comment = false
    may_be_in_comment = false
    may_be_out_of_multiline_comment = false
    for line in file:
        i = 0
        in_comment = false
        may_be_in_comment = false
        if in_multiline_comment:
            output.append(";")
        for char in line:
            if i == 0:
                if char == "/":
                    may_be_in_comment = true
            elif may_be_in_comment:
                if i == 1:
                    if char == "/":
                        output.append(";")
                        in_comment = true
                        may_be_in_comment = false
                    elif char == "*":
                        in_multiline_comment = true
            if in_comment and i > 1:
                output.append(char)
            if char == "*" and i == 0:
                may_be_out_of_multiline_comment = true
            if may_be_out_of_multiline_comment and i == 1:
                if char == "/":
                    in_multiline_comment = false
                    may_be_out_of_multiline_comment = false
            i += 1
        output.append("\n")

    return output

def parse(file):
    output = ""
    for char in file:
        output += char
        print(char)
    return output

if __name__ == "__main__":
    if sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as file:
            if sys.argv[3] == "-o":
                with open(sys.argv[4], "w") as output:
                    output.write(parse(lex(file.readlines())))
