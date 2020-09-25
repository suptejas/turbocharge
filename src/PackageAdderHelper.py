from collections import OrderedDict

def sort_packages(dictionary):
    full_len = 30

    dictionary = OrderedDict(sorted(dictionary.items()))

    print('-------------------------------')

    for key, value in dictionary.items():
        output = f'| {key}'

        chars_num = len(output)

        margin = full_len - chars_num

        chars = output.split()
        chars.insert(1, ' ')

        for _ in range(0, margin):
            chars.append(' ')

        chars.append('|')

        print("".join(chars))

    print('-------------------------------')