import re
txt = "abbb ab a bb bs bba"
x = re.findall(r"\bab*\b", txt)
print(x)