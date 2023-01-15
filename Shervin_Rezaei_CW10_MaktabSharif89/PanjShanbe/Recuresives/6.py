def is_it_prime(number, i=2):
    if number == i:
        return f"{number} is Prime!"
    elif number % i == 0:
        return f"{number} is Not Prime! \nCheck {number} / {i}."
    return is_it_prime(number, i + 1)


num = int(input("Write a number: "))
print(is_it_prime(num))
