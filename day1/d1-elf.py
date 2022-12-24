import json
from dataclasses import dataclass
from typing import List


@dataclass
class Elf:
    name: str
    foodbag: List[int]

    def caloriecount(self):
        return sum(self.foodbag)

@dataclass
class ElfPack:
    members: List[Elf]

    def calorie_max(self):
        """
        Returns: str,str
        with :
            - str : index of elf carrying most calories
            - str : caloriecount of heaviest elf
        """
        calcount = 0
        calindex = 0
        for elf_number, elf in enumerate(self.members):
            if elf.caloriecount() > calcount:
                calindex = elf_number
                calcount = elf.caloriecount()

        return calindex, calcount

    def get_calorie_list(self):
        """
        Return a list of total amount of calories per elf
        """
        callist = []
        for member in self.members:
            callist.append(sum(member.foodbag))

        return sorted(callist)

    def get_top3_elves(self):
        a = self.get_calorie_list()
        return sum(sorted(a)[-3:])



def read_input():
    with open('/Users/bcg213/src/python/acoc2022/d1-input.txt') as f:
        lines = f.readlines()

    index = 0
    tmp_elves = ElfPack(members=[ Elf('foo',[]) ])

    for line in lines:
        if line.strip():
            # non-empty line:
            tmp_elves.members[index].foodbag.append(int(line.strip()))
        else:
            # empty line, lets name our elf and start a new one
            tmp_elves.members[index].name = f"Elf_{index}"
            index += 1
            tmp_elves.members.append(Elf('foo', []))

    return tmp_elves


if __name__ == '__main__':
    elves = read_input()

    heavy_index, heavy_cal = elves.calorie_max()

    print(elves.members[0])
    print(f"DAY1 : Elf {heavy_index} is carrying {heavy_cal} calories.")
    #print(f"DAY2 : Top3 elves have total of {elves.get_calorie_list()} calories.")
    print(f"DAY2 : Top3 elves have total of {elves.get_top3_elves()} calories.")

