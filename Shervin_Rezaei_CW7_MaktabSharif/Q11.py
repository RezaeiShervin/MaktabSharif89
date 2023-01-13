import re

my_string = input('enter a string: ')
re_obj = re.compile('^\w+.*')
if re_obj.match(my_string):
    print('Matched!')
else:
    print('Not Matched!')
