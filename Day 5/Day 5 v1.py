import numpy as np

x = []
SEATS = np.zeros((128, 8))
for SEAT in open('SEATS.csv','r').readlines():
    Row = list(range(128))
    Col = list(range(8))
    for i in range(len(SEAT)):
        if i <= 6:
            if SEAT[i] == 'F' :
                Row = Row[0:len(Row)//2]
            else:
                Row = Row[len(Row)//2::]
        else:
            if SEAT[i] == 'L':
                Col = Col[0:len(Col)//2]
            else:
                Col = Col[len(Col)//2::]
    x.append(Row[0] *8 +Col[0])
    SEATS[Row,Col] = 1
print(max(x))
SEATS[:2] =1
SEATS[-6:] =1          
print(np.where(SEATS == 0))   
    
                
            