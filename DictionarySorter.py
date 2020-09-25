from collections import OrderedDict

dictionary = eval(input('Dictionary: '))
sorteddictionary = dict(OrderedDict(sorted(dictionary.items())))
print('{')
for key,value in sorteddictionary.items():
    print(f'    \'{key}\': \'{value}\',')
print('}')