import csv
#%% part 1
toc = 0
with open('PSW.csv','r') as myFile:
    for PSW in csv.reader( (line.replace('-', ':') for line in myFile)):
        for PSW in csv.reader( (line.replace(' ', ':')for line in PSW), delimiter =':'):
            N = PSW[4].count(PSW[2])
            if N >= int(PSW[0]):
                if N <= int(PSW[1]):
                    toc = toc + 1
                    
print('answer 1 = ', toc)
#%% part 2
toc =0
with open('PSW.csv','r') as myFile:
    for PSW in csv.reader( (line.replace('-', ':') for line in myFile)):
        for PSW in csv.reader( (line.replace(' ', ':')for line in PSW), delimiter =':'):
            string = PSW[4]   
            if PSW[2] == string[int(PSW[0])-1]:
                if PSW[2] != string[int(PSW[1])-1]:
                    toc = toc + 1
            if PSW[2] == string[int(PSW[1])-1]:
                if PSW[2] != string[int(PSW[0])-1]:
                    toc = toc + 1
print('answer 2 = ', toc)