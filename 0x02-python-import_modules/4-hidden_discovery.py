#!/usr/bin/python3
import hidden_4


def producer(hidden_4):
    for i in dir():
        if not (i[0] == '-' and i[1] == '-'):
            print(i)


if __name__ == "__main__":
    producer()
