import pandas as pd
from analyze import get_tokens

def e():
    exit(1)


def error():
    print("String Not Valid")


def valid():
    print("\nValid String")


def empty_stack_check(stack, string, index):
    if len(stack) == 0 and string[index] == '$':
        valid()
        e()
    elif len(stack) == 0:
        error()
        e()


def push_into_stack(string2, stack, terminals):
    if string2 in terminals:
        stack.append(string2)
    else:
        for x in string2[::-1]:
            if x != ' ':
                stack.append(x)
            else:
                error()
                e()


def adding_terminals(data_frame, terminals):
    for t in data_frame.keys():
        terminals.append(t)


def main():
    file = 'table2.xlsx'
    read = pd.ExcelFile(file)
    data_frame = read.parse('Sheet1')
    print(data_frame)
    terminals = ['!']
    adding_terminals(data_frame, terminals)
    string = get_tokens()
    index = 0
    stack = ['S']

    while index < len(string):
        empty_stack_check(stack, string, index)
        try:
            check = stack.pop()
            if check not in terminals:
                string2 = data_frame[string[index]][check]
                push_into_stack(string2, stack, terminals)
            else:
                if check != '!':
                    index += 1
        except():
            pass
    valid()


if __name__ == '__main__':
    main()
