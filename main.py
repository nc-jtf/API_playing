# This is a sample Python script.
import json


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def filter_list(l):
    new_l = []
    'return a new list with the strings filtered out'
    for i in l:
        if isinstance(i, int):
            new_l.append(i)
    return new_l

def unique_in_order(sequence):
    unique_sequence = []
    for i in sequence:
        for e in unique_sequence:
            if i == e:
                pass
            else:
                unique_sequence.append(i)

    return unique_sequence
if __name__ == '__main__':
    # print(unique_in_order('aaaeeee'))
    unique_in_order('aaaeeee')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
