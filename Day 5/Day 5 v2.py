import numpy as np
SEAT = open('SEATS.csv','r').read().replace('B','1').replace('F','0').replace('L','0').replace('R','1').split()
x = []
SEATS = np.zeros((128, 8))
for i in range(len(SEAT)):
    ROW = int(SEAT[i][0:7],2)
    Col = int(SEAT[i][7::],2)
    SEATS[ROW,Col] = 1 
    x.append(ROW*8 + Col)
print ('max id = ', max(x))
SEATS[0:2] =1
SEATS[120:128] =1    
print(np.where(SEATS == 0))    


    


    
                
            