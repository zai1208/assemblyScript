#!/usr/bin/python3
"""
Copyright (C) 2024 zai1208

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.
"""
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
