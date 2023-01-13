import re
my_string = input('enter a string ')
m = re.search('\b\w+[.!?,;]*$', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')