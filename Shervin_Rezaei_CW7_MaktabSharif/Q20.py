import re
my_string = 'The quick brown fox jumps over the lazy dog.'
m = re.search('cat|dog|fox|horse', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')