with open ("PASSP.txt",'r') as PASSP:
    PASSPO = PASSP.read().replace('\n\n','\r').replace('\n',' ').split('\r')
# #%%
# REQ = ['byr', 'iyr', 'eyr', 'hcl', 'hgt', 'ecl', 'pid']
# toc = 0
# for PASSPOR in PASSPO:
#     tic  = 0
#     for i in range(len(REQ)):
#         if REQ[i] in PASSPOR:
#           tic = tic + 1
#           if tic == len (REQ):
#               toc = toc + 1
             
             
# %%   
REQ = ['byr', 'iyr', 'eyr', 'hcl', 'hgt', 'ecl', 'pid']
toc = 0
for PASSPOR in PASSPO:
    tic  = 0
    for i in range(len(REQ)):
        if REQ[i] in PASSPOR:
          tic = tic + 1
          if tic == len (REQ): # all variables present
          
              PASSPORT = PASSPOR.split(" ")
              tac = 0
              
              for j in range(len(PASSPORT)):
                  
                  if PASSPORT[j][0:3] =='ecl':
                      if any(x in PASSPORT[j][4::] for x in ['amb','blu', 'brn','gry', 'grn', 'hzl', 'oth']):
                          tac = tac +1
                          
                  elif PASSPORT[j][0:3] =='pid':
                      if len(PASSPORT[j][4::]) == 9:
                          tac = tac +1 
                      
                  elif PASSPORT[j][0:3] =='hcl':
                      if PASSPORT[j][4] == '#':
                          if len(PASSPORT[j][5::]) == 6:   ##
                              count = 0
                              for k in range(len(PASSPORT[j][5::])):
                                  if any(x in PASSPORT[j][5+k] for x in ['0', '1','2','3','4','5','6','7','8','9' , 'a', 'b', 'c', 'd', 'e','f']):
                                      count = count+1
                                      if count == 6:
                                          tac =tac+1
                              
                  elif PASSPORT[j][0:3] =='hgt':
                      if PASSPORT[j][-2::] == 'cm':
                          if 150 <= int(PASSPORT[j][4:-2]) <= 193:
                              tac = tac+1
                      elif PASSPORT[j][-2::] == 'in':
                          if 59 <=int(PASSPORT[j][4:-2])<= 76:
                              tac = tac+1

                  elif PASSPORT[j][0:3] =='eyr':
                      if 2020 <=int(PASSPORT[j][4::]) <= 2030:
                          tac = tac +1
                          
                  elif PASSPORT[j][0:3] =='iyr':
                      if 2010 <=int(PASSPORT[j][4::]) <= 2020:
                          tac = tac +1
                          
                  elif PASSPORT[j][0:3] =='byr':
                      if 1920 <=int(PASSPORT[j][4::]) <= 2002:
                          tac = tac +1   
                          
                          
              if tac == 7:
                      toc = toc +1
                          
print(toc)
              
              
              
    