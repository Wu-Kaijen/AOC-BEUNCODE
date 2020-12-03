import csv
ROAD = []
for LAND in csv.reader(open('C:/Users/wukai/OneDrive - Universiteit Twente/Code/Python/AOC/Day 3/LANDSCAPE.csv', 'r')):
    ROAD.append(LAND[0])
    
# print(ROAD)
for j in range(len(ROAD)):
    ROAD[j] = ROAD[j] * 500
       

x = []
for j in range(1,len(ROAD)):
    jj = j
    x.append(ROAD[j][jj])        
N1 =x.count('#')

x = []
for j in range(1,len(ROAD)):
    jj = j*3
    x.append(ROAD[j][jj])
N2 =x.count('#')

x = []
for j in range(1,len(ROAD)):
    jj = j*5
    x.append(ROAD[j][jj])
N3 =x.count('#')

x = []
for j in range(1,len(ROAD)):
    jj = j*7
    x.append(ROAD[j][jj])
N4 =x.count('#')

x = []
for j in range(1,len(ROAD)//2 +1):
    jj = j*2
    x.append(ROAD[jj][j])
N5 =x.count('#')

print(N1*N2*N3*N4*N5)
