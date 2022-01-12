# Sum of numbers

def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

# Factorial

def factorial(n)
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# Fibonacci

def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))
