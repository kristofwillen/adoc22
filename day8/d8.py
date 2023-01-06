with open('input.d81', 'r') as f:
    input = f.readlines()

grid = [[ int(c) for c in r.strip()] for r in input]

def is_visible(matrix, i,j):
    is_visible_all = is_visible_from_top(matrix, i, j) or is_visible_from_bottom(matrix, i, j) or is_visible_from_left(matrix,i,j) or is_visible_from_right(matrix,i,j)
    return is_visible_all

def is_visible_from_top(matrix, i,j):
    isvisible = True
    for r in range(i):
        #print(f"{matrix[i][j]}>{matrix[r][j]}?")
        isvisible = isvisible and matrix[i][j] > matrix[r][j]
    if isvisible:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is visible from top")
    else:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is not visible from top")

    return isvisible

def is_visible_from_bottom(matrix, i,j):
    isvisible = True
    for r in range(i, len(matrix)+2):
        #print(f"{matrix[i][j]}>{matrix[i][c]}?")
        isvisible = isvisible and matrix[i][j] > matrix[r][j]
    if isvisible:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is visible from bottom")
    else:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is not visible from bottom")


def is_visible_from_left(matrix, i,j):
    isvisible = True
    for c in range(j):
        #print(f"{matrix[i][j]}>{matrix[i][c]}?")
        isvisible = isvisible and matrix[i][j] > matrix[i][c]
    if isvisible:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is visible from left")
    else:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is not visible from left")

    return isvisible

def is_visible_from_right(matrix, i,j):
    isvisible = True
    for c in range(j,len(matrix)+2):
        #print(f"{matrix[i][j]}>{matrix[i][c]}?")
        isvisible = isvisible and matrix[i][j] > matrix[i][c]
    if isvisible:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is visible from right")
    else:
        print(f"Elem {matrix[i][j]} [{i}][{j}] is not visible form right")

    return isvisible


visible = [[c for c in r] for r in grid]

print(visible)
for i,row in enumerate(grid):
    for j,item in enumerate(row):
        #print(f"[{i}][{j}]")
        if is_visible(grid, i ,j):
            visible[i][j] = 1
        else:
            visible[i][j] = 0
        if (i == 0) or (i == len(grid)-1):
            visible[i][j] = 1
        if (j == 0) or (j == len(visible[i])-1):
            visible[i][j] = 1


count = 0
for i in range(len(visible)):
    for j in range(len(visible[i])):
        if visible[i][j] == 1:
            count += 1

print(visible)
print(f"Nr of visible trees: {count}")