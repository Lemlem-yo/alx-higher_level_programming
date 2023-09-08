#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    sum = 0

    for arg in args:
        argu = int(arg)
        sum += argu

print(f"{sum}")
