#!/usr/bin/python3

for x in range(1, 101):
    print(["", "Fizz"][x % 3 == 0] + ["", "Buzz"][x % 5 == 0] or str(x))