import re
txt = "avrb ab a bb bs ba bbba"
x = re.findall(r"\ba\w+b\b", txt)
print(x)