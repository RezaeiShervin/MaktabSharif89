#! /usr/bin/python
import re

with open("Iran.txt","r") as txt:
    txt = txt.read()
    txt = re.sub(r"_"," ", txt)
    txt = re.findall(r"\b[A-Z]+\w+\b", txt)
    txt = [f"{x}\n" for x in txt]
    txt = set(txt)
with open("Iran_cap.txt", "w") as f:
    f.writelines(txt)
