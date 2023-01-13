import re
txt = "abbb ab a bb bs ba bbba"
x = re.findall(r"\bb{3}a\b", txt)
print(x)