import re
txt = "abc_def ab a bb bs ba bbba acd_def"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x)