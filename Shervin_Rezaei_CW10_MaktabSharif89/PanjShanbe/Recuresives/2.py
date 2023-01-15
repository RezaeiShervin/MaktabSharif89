def product(x, y):

	if y != 0:
		return (x * product(x, y - 1))
	elif x == 0:
		return 0
	else:
		return 1
x = 2
y = 21

print(product(x, y))