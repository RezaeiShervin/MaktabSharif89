def fibonacci(entry_number):
    if entry_number == 0:
        return 0
    elif entry_number == 1:
        return 1
    return fibonacci(entry_number - 1) + fibonacci(entry_number - 2)


n = int(input("Write an integer number: "))
print(fibonacci(n))  # Check https://www.calculatorsoup.com/calculators/discretemathematics/fibonacci-calculator.php

