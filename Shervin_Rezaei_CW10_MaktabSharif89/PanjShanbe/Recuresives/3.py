def product(x):
    if x>=0:
        print(x, end='\t')
        product(x-1)


x = 5
product(x)