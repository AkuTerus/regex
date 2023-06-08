import re
def validasi_kartu_kredit(nomor_kartu):
    if len(nomor_kartu) !=16 :
        return "Tidak valid"
    elif not re.match(r"^[4-6]\d{16}$", nomor_kartu):
        return "tidak valid"
    elif re.search(r"8{4}", nomor_kartu):
        return 'Valid Platinum'
    else:
        return 'Valid Reguler'
# nomor_kartu = '4388884888814526'

def validasi_kartu_kredit(nomor_kartu):
    try :
        nomor_kartu == int(nomor_kartu)
    except:
        return "Tidak valid" 

    kartu = str(nomor_kartu)
    if len(kartu) !=16:
        return 'Tidak valid'
    else:
        if kartu[0] in "456":
            if "8888" in kartu:
                return 'Valid Platinum'
            else:
                return 'Valid Reguler'
        else:
            return 'Tidak valid'
nomor_kartu = '588818880888888'

print(len(nomor_kartu))
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)
