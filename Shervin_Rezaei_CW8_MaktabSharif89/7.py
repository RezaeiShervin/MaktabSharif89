 
import re


def getNumbers(str):
    array = re.findall(r'[0-9]+', str)
    return array


str = input(">>>")
array = getNumbers(str)
print(*array)
