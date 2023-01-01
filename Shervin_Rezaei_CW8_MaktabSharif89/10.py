 
import re

street = input(">>>")
print(re.sub('Road$', 'Rd .', street))
