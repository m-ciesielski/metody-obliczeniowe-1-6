# -*- coding: utf-8 -*-
import numpy


def calculate_function_value(x):
    """
    Oblicza wartość funkcji x+log(x)-4 dla podanej wartości x.
    :rtype : float - wartość funkcji x+log(x)-4
    """
    return x+numpy.log(x)-4


def calculate_derivative_function_value(x):
    """
    Oblicza wartość pochodnej funkcji x+log(x)-4 dla podanej wartości x.
    Pochodna jest określona wzorem 1+(1/x).
    :rtype : float - wartość funkcji 1+(1/x)
    """
    return 1+(1/x)


def simple_iteration(x):
    """
    Oblicza wartość funkcji punktu stałego (4-log(x)).
    :rtype : float = wartośc funkcji 4-log(x)
    """
    return 4-numpy.log(x)


def calculate_simple_iterations(x, iterations_limit=10):
    """
    Wykonuje metodę iteracji prostych. Ilość iteracji jest określona przez argument iterations_limit.
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    start_point = x
    result = None
    for i in range(0, iterations_limit):
        result = simple_iteration(start_point)
        start_point = result
    return result


def secant_method(x0, x1):
    """
    Wykonuje metodę siecznych dla podanych punktów początkowych x0 i x1.
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    f_x0_val = calculate_function_value(x0)
    f_x1_val = calculate_function_value(x1)

    return x1-((f_x1_val*(x1-x0))/(f_x1_val-f_x0_val))


def tangent_method(x):
    """
    Wykonuję metodę stycznych dla podanego punktu początkowego x.
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    return x - (calculate_function_value(x)/calculate_derivative_function_value(x))


def parse_user_provided_float(label):
    """
    Funkcja pomocnicza wczytującą podawaną przez użytkownika wartość typu float.
    :rtype : float
    """
    val = None
    while True:
        try:
            val = float(input("Podaj wartość {0}:".format(label)))
        except ValueError:
            print("Wpisz poprawną wartość {0}.".format(label))
            continue
        else:
            break

    return val

if __name__ == '__main__':
    simple_iterations_start_point = parse_user_provided_float("punktu startowego metody iteracji prostych")
    print(calculate_simple_iterations(simple_iterations_start_point))

    x0_secant = parse_user_provided_float("x0 dla metody siecznych")
    x1_secant = parse_user_provided_float("x1 dla metody siecznych")
    print(secant_method(x0_secant, x1_secant))

    tangent_starting_point = parse_user_provided_float("punktu startowego metody stycznych")
    print(tangent_method(tangent_starting_point))
