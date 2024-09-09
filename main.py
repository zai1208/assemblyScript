#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if sys.argv[1] == "-f":
        with open(sys.argv[2], "r") as file:
            if sys.argv[3] == "-o":
                with open(sys.argv[4], "w") as output:
                    output.write(file.read())
