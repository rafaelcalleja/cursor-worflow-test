# src/fizzBuzz.py

def fizzbuzz(number: int):
    """Calculates the FizzBuzz result for a given integer.

    Args:
        number: The integer to evaluate.

    Returns:
        "Fizz" if the number is divisible by 3.
        "Buzz" if the number is divisible by 5.
        "FizzBuzz" if the number is divisible by both 3 and 5.
        The number itself otherwise.
    """
    # [RATIONALE] Check for divisibility by 15 first (3*5) to handle the
    # "FizzBuzz" case correctly. Otherwise, numbers divisible by 15 would
    # incorrectly return "Fizz" or "Buzz" based on the order of checks.
    if number % 15 == 0:
        return "FizzBuzz"
    # Check for divisibility by 3
    elif number % 3 == 0:
        return "Fizz"
    # Check for divisibility by 5
    elif number % 5 == 0:
        return "Buzz"
    # Otherwise, return the number itself
    else:
        return number 