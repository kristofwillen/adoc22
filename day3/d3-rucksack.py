
def get_compartiment(r):
    return r[:len(r)//2], r[len(r)//2:]

def get_commons(r1, r2):
    return list(set(r1) & set(r2))

def get_badge(l1, l2, l3):
    return list(set(l1) & set(l2) & set(l3))


def get_prio(item):
    if item.isupper():
        ordchar = ord(item) - 38
    else:
        ordchar = ord(item) - 96

    return ordchar

def get_rucksack_prio(commons):
    priority = 0
    for item in commons:
        priority += get_prio(item)

    return priority


if __name__ == '__main__':

    with open('d3-input.txt', 'r') as f:
        sacks = f.read().split('\n')

    answer = 0
    answer2 = 0
    for index, rucksack in enumerate(sacks):
        r1, r2 = get_compartiment(rucksack)
        answer += get_rucksack_prio(get_commons(r1, r2))

        if index % 3 == 2:
            badge = get_badge(sacks[index-2], sacks[index-1], sacks[index])
            print(f"Found badge {badge} for group {sacks[index-2]} -  {sacks[index-1]} -  {sacks[index]}")
            answer2 += get_prio(badge[0])

    print(answer)
    print(answer2)



