import re
def cek_kodepos(kodePos):
    if len(kodePos) == 5:
        total = 0
        for i in range(len(kodePos) -2 ):
            if kodePos[i] == kodePos[i+2]:
                total +=1
        if total >1:
            print('Tidak Valid')
        else:
            print('Valid')

print(cek_kodepos('12145'))