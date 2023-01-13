import re
my_string = input('enter a string ')
m = re.search('[0-9]{1,3}', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')