# -------------------------------------------------------------------------
# tc numarasının checksum kısmını hesaplayan kısım

import random

def tc_generator():
        
    def tcno_checksum(tcno):
        tc    = '%d' % tcno
        tc10  = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
        tc10 *= 7
        tc10 -= int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
        tc10 %= 10

        tc11  = int(tc[0]) + int(tc[1]) + int(tc[2]) + int(tc[3]) + int(tc[4])
        tc11 += int(tc[5]) + int(tc[6]) + int(tc[7]) + int(tc[8]) + int(tc10)
        tc11 %= 10

        return '%s%d%d' % (tc, tc10, tc11)


    # -------------------------------------------------------------------------
    # akrabalarin tc numara listesini donduren bolum
    def akraba_tcno(tcno, adet):
        akraba_liste = []
        tc   = int(tcno[0:-2])
        t    = tc - 29999 * (1 + int(adet / 2))
        for i in range(adet+1):
            t += 29999
            atc = tcno_checksum(t)
            akraba_liste.append(atc)

        return akraba_liste

        

    tc_no=["68416560860","18198483956","26173613144","86443147298","43556609648","88308455180"]
    data=[]
    for a in tc_no:
        for i in akraba_tcno(a,3000):
            data.append(i)
             
    return random.choice(data)