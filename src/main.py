import sys

if __name__ == "__main__":
	if sys.argv[1] == "-f":
		with open(sys.argv[2], "r") as file:
			print(file.read())
