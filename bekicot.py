t = 100
s = 0
h= 0

while s < t:
    jam = 0;
    while jam <= 24 and s< t:
        if jam == 12:
            s += 5
            h += 1
        if jam == 24:
            s -= 4
        jam += 12
    print('hari '+str(hari)+' bekicot naik '+ str(sampai) +' meter')
