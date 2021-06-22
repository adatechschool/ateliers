#!/usr/bin/env python3

from typing import List, Union


EXPR = '98 - 6 * 8 * 1.5 + 4 - 1 / 5'
OPERATORS = ['+', '-', '*', '/']

# First step
def A(expr: str) -> List[str]:
    return expr.split()

assert A(EXPR) == ['98', '-',  '6',  '*', '8', '*', '1.5', '+', '4', '-', '1', '/', '5']

# Second step
def B(elements: List[str]) -> List[Union[str, float]]:
    result = []
    for element in elements:
        if element in OPERATORS:
            result.append(element)
        else:
            result.append(float(element))
    return result

assert B(A(EXPR)) == [98.0, '-',  6.0,  '*', 8.0, '*', 1.5, '+', 4.0, '-', 1.0, '/', 5.0]

# Thrid step

def add(operand1: float, operand2: float) -> float:
    print('ADD {} {}'.format(operand1, operand2))
    return operand1 + operand2

def minus(operand1: float, operand2: float) -> float:
    print('MINUS {} {}'.format(operand1, operand2))
    return operand1 - operand2

def multiply(operand1: float, operand2: float) -> float:
    return operand1 * operand2

def true_divide(operand1: float, operand2: float) -> float:
    return operand1 / operand2

# Fourth step

## Iterative

def _resolve_prioritary_operators(elements: List[Union[str, float]]) -> List[Union[str, float]]:
    intermediate_result = []
    i = 0
    while i <  len(elements):
        if elements[i] == '*':
            local_result = multiply(intermediate_result[-1], elements[i+1])
            intermediate_result[-1] = local_result
            i += 2
        elif elements[i] == '/':
            local_result = true_divide(intermediate_result[-1], elements[i+1])
            intermediate_result[-1] = local_result
            i += 2
        else:
            intermediate_result.append(elements[i])
            i += 1
            continue
    return intermediate_result

assert _resolve_prioritary_operators(B(A(EXPR))) == [98.0, '-', 72.0, '+', 4.0, '-', 0.2]

def _resolve_non_prioritary_operators(elements: List[Union[str, float]]) -> float:
    intermediate_result = elements[0]
    i = 0
    while i <  len(elements):
        if elements[i] == '+':
            intermediate_result = add(intermediate_result, elements[i+1])
            i += 2
        elif elements[i] == '-':
            intermediate_result = minus(intermediate_result, elements[i+1])
            i += 2
        else:
            i += 1
    return intermediate_result

assert _resolve_non_prioritary_operators([98.0, '-', 72.0, '+', 4.0, '-', 0.2]) == 29.8

def resolve_iterative(elements: List[Union[str, float]]) -> float:
    intermediate_result = _resolve_prioritary_operators(elements)
    return _resolve_non_prioritary_operators(intermediate_result)

assert resolve_iterative(B(A(EXPR))) == 29.8

## Reccursive

def resolve_reccursive(elements: List[Union[str, float]]) -> float:
    if len(elements) == 1:
        return elements[0]

    operand1, operator, remaining = elements[0], elements[1], elements[2:]
    print(operand1, operator, remaining)
    if operator in ['*', '/']:
        operand2 = remaining[0]
        if operator == '*':
            remaining[0] = multiply(operand1, operand2)
        elif operator == '/':
            remaining[0] = true_divide(operand1, operand2)
        print("Now resolving {}".format(remaining))
        return resolve_reccursive(remaining)
    elif operator == '+':
        print("Now resolving {}".format(remaining))
        return add(operand1, resolve_reccursive(remaining))
    elif operator == '-':
        print("Now resolving {}".format(remaining))
        return minus(operand1, resolve_reccursive(remaining))

print(resolve_reccursive(B(A(EXPR))))

# assert resolve_reccursive(B(A(EXPR))) == 29.8
