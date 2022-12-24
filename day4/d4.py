import numpy as np


def no_overlap(array1, array2):
    overlap_array = np.isin(array2, array1)+np.isin(array1, array2)
    return False in overlap_array


def input_to_array(inputline):
    try:
        range1, range2 = inputline.split(',')
    except ValueError:
        print(f"FAIL: {inputline}")
        raise ValueError
    r1begin, r1end = range1.split('-')
    r2begin, r2end = range2.split('-')
    return list(range(int(r1begin),int(r1end)+1)), list(range(int(r2begin),int(r2end)+1))

if __name__ == '__main__':
    # with open('d4-input.txt', 'r') as f:
    #     spaces = f.read().split('\n')

    # overlaps = 0
    # for space in spaces:
    #     range1, range2 = input_to_array(space)
    #     if no_overlap(range1, range2):
    #         overlaps += 0
    #     else:
    #         overlaps += 1
    #         print(f"({overlaps}) Found overlap at {space}")

    # print(f"Found {overlaps} overlaps")


    x = open("d4-input.txt", "r").read().splitlines()
    t = 0
    for i in x:
        a,b=i.split(",")

        aa, aaa = [int(r) for r in a.split("-")]
        bb, bbb = [int(r) for r in b.split("-")]

        if bbb >=aa  >= bb  or aaa >= bb>=aa:
            t+=1
    print(t)