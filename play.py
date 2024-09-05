#!/usr/bin/python3
import os
import sys

from playsound import playsound



def main():
	args = sys.argv[1:]
	if len(args) < 1:
		print(f"Usage:\n\tpython3 play.py song.mp3")
		return

	filepaths = args
	for filepath in filepaths:
		if os.path.isfile(filepath):
			print(f"Playing: '{filepath}'")
			playsound(filepath)
		else:
			print(f"Not found: '{filepath}'")


if __name__ == '__main__':
	main()
