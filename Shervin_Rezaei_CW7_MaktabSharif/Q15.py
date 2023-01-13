import re
my_string = input('enter a string ')
m = re.search('[^0-9A-Za-z_]+', my_string)
if m:
    print('no match found')
else:
    print('it\'s a match')