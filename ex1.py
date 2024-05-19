#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError(f"Значение должно быть не меньше {min_val}.")
            if max_val is not None and value > max_val:
                raise ValueError(f"Значение должно быть не больше {max_val}.")
            return value
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

def generate_matrix(rows, cols, min_val, max_val):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def main():
    print("Программа для генерации матрицы случайных целых чисел.")
    
    rows = get_int_input("Введите число строк: ", 1)
    cols = get_int_input("Введите число столбцов: ", 1)
    min_val = get_int_input("Введите минимальное значение диапазона: ")
    max_val = get_int_input("Введите максимальное значение диапазона: ", min_val)
    
    matrix = generate_matrix(rows, cols, min_val, max_val)
    
    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()
