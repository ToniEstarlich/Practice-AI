def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

if __name__ == '__main__':
    print('Testing calculator.py...')
    assert add(2, 3) == 5, 'Addition test failed'
    assert subtract(5, 3) == 2, 'Subtraction test failed'
    assert multiply(2, 3) == 6, 'Multiplication test failed'
    assert divide(6, 3) == 2, 'Division test failed'
    print('All tests passed.')