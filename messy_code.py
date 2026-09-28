def calculate(first_number, second_number):
    """Print the sum and product of two numbers."""
    if not isinstance(first_number, (int, float)) or not isinstance(
        second_number, (int, float)
    ):
        raise TypeError("Both arguments must be numbers.")

    total = first_number + second_number
    product = first_number * second_number

    print(f"Sum: {total}")
    print(f"Product: {product}")


calculate(10, 5)