#!/usr/bin/python3
import sys


def retrive():
    args = sys.argv[1:]
    num_args = len(args)
    print(f"{num_args} arguments:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    retrive()
