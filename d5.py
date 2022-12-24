
if __name__ == '__main__':
    with open('d5-input.txt', 'r') as f:
        input = f.read().split('\n')

    divider = input.index('')
    print('found divierder at index: ', str(divider))
    stacklines = input[:divider]
    movements = input[divider+1:]
    print()