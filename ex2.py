#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def main():
    value1 = input("Первое значение: ")
    value2 = input("Второе значение: ")

    try:
        num1 = float(value1)
        num2 = float(value2)
        result = num1 + num2
    except ValueError:
        result = value1 + value2

    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
