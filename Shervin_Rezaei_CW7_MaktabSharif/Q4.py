import re
txt = "abbb ab a bb bs bba"
x = re.findall(r"\bb+a\b", txt)
print(x)