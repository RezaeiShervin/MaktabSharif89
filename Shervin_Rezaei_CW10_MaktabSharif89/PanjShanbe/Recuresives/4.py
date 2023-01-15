def product(x):
    if x>=0:
        product(x-1)
        print(x, end='\t')


x = 5
product(x)