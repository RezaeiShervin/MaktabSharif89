 
import re

text = input(">>>")

for m in re.finditer("\d+", text):

    print(m.group(0))
    print("Index position:", m.start())
