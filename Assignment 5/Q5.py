cols,rows=3,3
matrix = [[int(input(f'Enter element at {r},{c}: ')) for c in range(cols)] for r in range(rows)]
print(matrix)
s=0
for i in range(rows):
    for j in range(cols):
        s+=matrix[j][i]
    print(s)
    s=0
    