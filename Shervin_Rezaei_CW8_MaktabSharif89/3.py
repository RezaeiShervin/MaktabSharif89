import re


def urlify(s):
    s = re.sub(r"\s+", '_', s)
    return s


def converter(a):
    a = re.sub(r"_", " ", a)
    return a


b = input(">>>")
if ' ' in b:
    print(urlify(b))
else:
    print(converter(b))
