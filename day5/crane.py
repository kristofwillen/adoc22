def create_crates_list(crates):
    nr_of_crates = (len(crates[0])+1)//4
    cratelist = []
    cratelist = [[] for i in range(nr_of_crates)]
    for line in crates:
        for crate in range(0,nr_of_crates):
            cratechar = line[list(crates[-1]).index(str(crate+1))]
            if cratechar != ' ' and cratechar not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                #print(f"Adding {cratechar} to crate {crate}...")
                cratelist[crate].append(cratechar)

    return cratelist


def moving(clist, nr, fromc, toc):
    for turn in range(nr):
        crate_to_move = clist[fromc][0]
        clist[fromc] = clist[fromc][1:]
        clist[toc] = [ crate_to_move ] + clist[toc]
    return clist

# -- main
if __name__ == "__main__":
    with open("./input.d5", "r", encoding="UTF-8") as str_file:
        # split on empty lines
        drawing = str_file.read().split("\n\n")

    crates = drawing[0].split("\n")
    procedure = drawing[1].split("\n")

    print(f"Number of crates => {(len(crates[0])+1)//4}")
    crateslist  = create_crates_list(crates)

    for action in procedure:
        try:
            [ movestr, nrofcrates, fromstr, fromcrate, tostr, tocrate ] = action.split(' ')
        except ValueError as e:
            print('kipping ...')
        else:
            crateslist = moving(crateslist, int(nrofcrates), int(fromcrate)-1, int(tocrate)-1)
        print(crateslist)

print(crateslist)
