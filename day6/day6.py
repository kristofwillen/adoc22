from dataclasses import dataclass

@dataclass
class Signal:
    code: str

    def decode_old(self):
        lrulist = []
        lruindex = 0
        index = 0
        stopindex = 0
        while index < len(self.code):
            somechar = self.code[index]
            print(f"Evaluating {lrulist}{somechar}")
            if somechar not in lrulist:
                lrulist.append(somechar)
                lruindex += 1
                index += 1

                if len(lrulist) >= 4:
                    print('')
                    print('Found 4 diffed chars at index: ', index)
                    return index
            else:
                print('')
                print(f"Found already char {somechar} at position {lruindex+1}, resetting...")
                print(somechar, end='')
                stopindex += 1
                lruindex = stopindex
                index = stopindex
                lrulist = [somechar]

    def decode(self):
        for index, somechar in enumerate(list(self.code)):
            charlist = list(self.code[index:index+4])
            uniquelist = list(set(charlist))

            #print(somechar, charlist, uniquelist)
            if len(charlist)>len(uniquelist):
                print('Found double char, resetting...')
            else:
                print(f"Evaluating {charlist}...")
                print(f"Found it => {index+4}")
                break
            if index >= len(list(self.code)):
                break

if __name__ == "__main__":
    with open('d6-input.txt', 'r') as f:
        code = f.readlines()

    #code = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
    #code = ['nppdvjthqldpwncqszvftbrmjlhg']
    #code = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
    #code = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']

    codelist = Signal(code=code[0])
    #foundit = codelist.decode()
    #print('Found it : ', foundit)
    codelist.decode()



