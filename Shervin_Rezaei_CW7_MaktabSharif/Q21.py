import re

my_string = 'The quick brown fox jumps over the lazy dog.'
m = re.search('\Wfox\W', my_string)
if m:
    print('it\'s a match, starts on', m.start())
else:
    print('no match found')
