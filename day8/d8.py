with open('input.d80', 'r') as f:
    input = f.readlines()

grid = [[ int(c) for c in r.strip()] for r in input]

def is_visible(matrix, i,j):
    is_visible_all = is_visible_from_top(matrix, i, j) or is_visible_from_bottom(matrix, i, j) or is_visible_from_left(matrix,i,j) or is_visible_from_right(matrix,i,j)
    return is_visible_all

def is_visible_from_top(matrix, i,j):
    isvisible = True
    if i == 0:
        return True
    else:
        top = [matrix[z][j] for z in range(i)]
        return max(top) < matrix[i][j]


def is_visible_from_bottom(matrix, i,j):
    isvisible = True
    if i == len(matrix) - 1:
        return True
    else:
        bottom = [matrix[z][j] for z in range(i+1, len(matrix))]
        return max(bottom)< matrix[i][j]


def is_visible_from_left(matrix, i,j):
    isvisible = True
    if j == 0:
        return True
    else:
        left = [matrix[i][z] for z in range(j)]
        return max(left) < matrix [i][j]

def is_visible_from_right(matrix, i,j):
    isvisible = True
    if j == len(matrix[i]) - 1:
        return True
    else:
        right = [matrix[i][z] for z in range(j+1, len(matrix[i]))]
        return max(right) < matrix[i][j]


visible = [[c for c in r] for r in grid]

print(visible)
for i,row in enumerate(grid):
    for j,item in enumerate(row):
        #print(f"[{i}][{j}]")
        if is_visible(grid, i ,j):
            visible[i][j] = 1
        else:
            visible[i][j] = 0


count = 0
for i in range(len(visible)):
    for j in range(len(visible[i])):
        if visible[i][j] == 1:
            count += 1

print(visible)
print(f"Nr of visible trees: {count}")