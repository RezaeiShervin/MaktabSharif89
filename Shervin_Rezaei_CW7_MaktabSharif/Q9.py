import re
txt = "abcABC ACDbac abcADCdf ABCadfRT bs ba bbba"
x = re.findall(r"\b[A-Z]+[a-z]+\b", txt)
print(x)