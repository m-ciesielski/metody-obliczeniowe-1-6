# -*- coding: utf-8 -*-
import numpy


def function_value(x):
    """
    Oblicza wartość funkcji x+log(x)-4 dla podanej wartości x. Zwraca NaN dla ujemnych argumentów, ponieważ logarytm
    liczby ujemnej nie jest liczbą rzeczywistą.

    :arg x : float
    :rtype : float - wartość funkcji x+log(x)-4
    """
    return x + numpy.log(x) - 4


def derivative_function_value(x):
    """
    Oblicza wartość pochodnej funkcji x+log(x)-4 dla podanej wartości x.
    Pochodna jest określona wzorem 1+(1/x).

    :arg x : float
    :rtype : float - wartość funkcji 1+(1/x)
    """
    return 1 + (1/x)


def simple_iteration(x):
    """
    Oblicza wartość funkcji punktu stałego (4-log(x)). Zwraca NaN dla ujemnych argumentów, ponieważ logarytm
    liczby ujemnej nie jest liczbą rzeczywistą.

    :arg x : float
    :rtype : float = wartośc funkcji 4-log(x)
    """
    return 4 - numpy.log(x)


def calculate_simple_iterations(x, iterations_limit=10):
    """
    Wykonuje metodę iteracji prostych. Ilość iteracji jest określona przez argument iterations_limit.

    :arg x : float
    :arg iterations_limit : int
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    start_point = x
    result = None
    for i in range(0, iterations_limit):
        result = simple_iteration(start_point)
        if result < 0:
            print("Metoda nie jest zbieżna dla danego punktu początkowego.")
            break
        start_point = result
    return result


def secant_method(x0, x1):
    """
    Wykonuje metodę siecznych dla podanych punktów początkowych x0 i x1.

    :arg x0 : float
    :arg x1 : float
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    return x1 - ((function_value(x1) * (x1-x0)) / (function_value(x1) - function_value(x0)))


def calculate_secant_iterations(x0, x1, iterations_limit=10):
    """
    Wykonuje iterację metody siecznych. Ilość iteracji jest określona przez argument iterations_limit.
    Argumenty x0 i x1 to punkty startowe metody.

    :arg x0 : float
    :arg x1 : float
    :arg iterations_limit : int
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    result = None
    # Zmienna x_k_min_1 reprezentuję wartość x_{k-1}.
    x_k_min_1 = x0
    x_k = x1
    for i in range(0, iterations_limit):
        result = secant_method(x_k_min_1, x_k)
        x_k_min_1 = x_k
        x_k = result
        if x_k == x_k_min_1:
            break
    return result


def tangent_method(x):
    """
    Wykonuję metodę stycznych dla podanego punktu początkowego x.

    :arg x : float
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    return x - (function_value(x) / derivative_function_value(x))


def calculate_tangent_iterations(x, iterations_limit=10):
    """
    Wykonuje iterację metody stycznych. Ilość iteracji jest określona przez argument iterations_limit.

    :arg x : float - Punkt startowy
    :arg iterations_limit : int
    :rtype : float - przybliżona wartość miejsca zerowego
    """
    start_point = x
    result = None
    for i in range(0, iterations_limit):
        result = tangent_method(start_point)
        start_point = result
        if result < 0:
            print("Metoda nie jest zbieżna dla danego punktu początkowego.")
            break
    return result


def parse_user_provided_float(label):
    """
    Funkcja pomocnicza wczytującą podawaną przez użytkownika wartość typu float.

    :arg label : string
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

    x0_secant = parse_user_provided_float("punktu startowego x0 dla metody siecznych")
    x1_secant = parse_user_provided_float("punktu startowego x1 dla metody siecznych")
    print(calculate_secant_iterations(x0_secant, x1_secant))

    tangent_starting_point = parse_user_provided_float("punktu startowego metody stycznych")
    print(calculate_tangent_iterations(tangent_starting_point))
