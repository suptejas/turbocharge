from collections import OrderedDict

dictionary = eval(input('Dictionary: '))
complete = 30
dictionary = OrderedDict(sorted(dictionary.items()))
print('-------------------------------')
for key, value in dictionary.items():
    output = f'| {key}'
    numberofcharacters = len(output)
    whitespaces = complete - numberofcharacters
    listofcharacters = output.split()
    listofcharacters.insert(1, ' ')
    for _ in range(0, whitespaces):
        listofcharacters.append(' ')
    listofcharacters.append('|')
    string = ''
    print(string.join(listofcharacters))
print('-------------------------------')