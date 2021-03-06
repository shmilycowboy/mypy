
num_dict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
}

num_str = input('input a number:')
for ch in num_str:
    print(num_dict[ch], end='')
