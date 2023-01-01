import re
string = "Python exercise, C# exercise, type-script exercise"
sub_str = input("Enter word:")
raw_s = fr"{sub_str}"
list_of_words = re.findall(raw_s, string)
if len(list_of_words) > 1:
    print(f'''
    {list_of_words[0]}
repetition: {len(list_of_words)}''')
else:
    print("Not found")
