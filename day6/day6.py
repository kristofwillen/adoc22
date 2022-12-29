from dataclasses import dataclass

@dataclass
class Signal:
    code: str

    def decode(self):
        lrulist = []
        lruindex = 0
        index = 0
        stopindex = 0
        while index < len(self.code):
            somechar = self.code[index]
            if somechar not in lrulist:
                lrulist.append(somechar)
                lruindex += 1

                print(somechar, end='')
                if lruindex >= 4:
                    print('')
                    print('Found 4 diffed chars at index: ', index+1)
                    return index+1
            else:
                print('')
                print(f"Found already char {somechar} at position {lruindex+1}, resetting...")
                print(somechar, end='')
                stopindex += 1
                lruindex = stopindex
                lrulist = [somechar]

if __name__ == "__main__":
    #with open('d6-input.txt', 'r') as f:
    #    code = f.readlines()

    code = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
    #code = ['nppdvjthqldpwncqszvftbrmjlhg']
    codelist = Signal(code=code[0])
    foundit = codelist.decode()
    print('Found it : ', foundit)



