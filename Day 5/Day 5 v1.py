import math
import numpy as np

#%% part 1
x = []
with open('SEATS.csv','r') as SEAT:
    for SEAT in SEAT.readlines():
        Row = list(range(128))
        Col = list(range(8))
        for i in range(len(SEAT)):
            if i <= 6:
                if SEAT[i] == 'F' :
                    Row = Row[0:math.floor(len(Row)//2)]
                else:
                    Row = Row[math.ceil(len(Row)//2)::]
            else:
                if SEAT[i] == 'L':
                    Col = Col[0:math.floor(len(Col)//2)]
                else:
                    Col = Col[math.ceil(len(Col)//2)::]
        x.append(Row[0] *8 +Col[0])
# print(max(x))

#%%  2
x = np.zeros((128, 8))
with open('SEATS.csv','r') as SEAT:
    for SEAT in SEAT.readlines():
        Row = list(range(128))
        Col = list(range(8))
        for i in range(len(SEAT)):
            if i <= 6:
                if SEAT[i] == 'F' :
                    Row = Row[0:math.floor(len(Row)//2)]
                else:
                    Row = Row[math.ceil(len(Row)//2)::]
            else:
                if SEAT[i] == 'L':
                    Col = Col[0:math.floor(len(Col)//2)]
                else:
                    Col = Col[math.ceil(len(Col)//2)::]
        x[Row,Col] = 1
x[0:2] =1
x[120:128] =1        
a,b= np.where(x == 0)
x = [a,b]



    
                
            