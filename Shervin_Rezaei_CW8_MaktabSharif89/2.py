
import re

string = "Python exercise, C# exercise, type-script exercise"
sub_str = input("Enter word:")
raw_s = fr"{sub_str}"

list_of_words = re.findall(raw_s, string)
if len(list_of_words) > 1:
    print(f'''
    {list_of_words[0]}
    occurrence: {len(list_of_words)}\n''')
else:
    print("Not found")

count = 1
for match in re.finditer(raw_s, string):
    span = match.span()
    print(f"{count}.Positions of {list_of_words[0]}: {span}")
    count += 1
