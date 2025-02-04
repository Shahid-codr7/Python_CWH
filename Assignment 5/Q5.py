cols,rows=4,3
matrix = [[int(input(f'Enter element at {r},{c}: ')) for c in range(cols)] for r in range(rows)]
print(matrix)
s=0
for i in range(cols):
    for j in range(rows):
        s+=matrix[j][i]
    print(s)
    s=0
    