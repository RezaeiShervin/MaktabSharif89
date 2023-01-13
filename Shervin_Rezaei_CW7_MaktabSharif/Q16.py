import re
my_string = input('enter a string ')
my_number = input('enter a number ')
pattern = '\b{}\b'.format(my_number)
rstring = r'{}'.format(pattern)
m = re.match(my_number, my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')