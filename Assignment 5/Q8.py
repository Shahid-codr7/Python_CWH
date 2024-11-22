import random,sys
rows,cols=4,4
matrix=[[random.randint(0,1) for j in range(cols)]for  i in range(rows)]
for i in range(len(matrix)):
    print(matrix[i])

c1=0
c2=0
sr=0
sc=0
maxr=-sys.maxsize-1
maxc=-sys.maxsize-1

for i in range(rows):
    for j in range(cols):
        sr+=matrix[i][j]
        sc+=matrix[j][i]
    if sr > maxr:
        maxr=sr
        maxrow=i
      
    if sc > maxc:
        maxc=sc
        maxcol=i
        
    sr=0
    sc=0
print(f'Largest row index: {maxrow}\nLargest column index: {maxcol}')

