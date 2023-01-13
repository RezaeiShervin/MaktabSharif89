import re
txt = "abbb ab a bba bs ba bbba"
x = re.findall(r"\bb{2,3}a\b", txt)
print(x)