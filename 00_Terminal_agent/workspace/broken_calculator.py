def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


if __name__ == "__main__":
    print("Testing calculator...")

    assert add(2, 3) == 5
    assert multiply(2, 3) == 6
    assert divide(10, 2) == 5

    print("All tests passed.")