import re
my_IP = input('enter a string ')
my_clean_IP = re.sub('\.0*', '.', my_IP)
print(my_clean_IP)