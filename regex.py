import re
def baca_file(nama_file):
    handle = open(nama_file,"r")
    artikel = handle.read()
    handle.close()
    return artikel

nama_file = "berita.txt"
artikel = baca_file(nama_file)
# print(artikel)
# 1. Tampilkan semua kata yang di awali huruf besar
pettern = r"[A-Z]\w+"
hasil =re.findall(pettern, artikel)
print(f'Ditemukan {len(hasil)} kata yang diawaili huruf nesar')
# print(hasil)
# 2. tampilkan informsai tanggal
tanggal = r"\d\d?/\d\d?/\d\d\d\d"
hasil2 = re.findall(tanggal, artikel)
print(f'Di temukan tanggal sebanyak {len(hasil2)}')
print(hasil2)

# 3. Tampilkan semua kata yang panjangnya 7
pattern3 = r"\b[A-Za-z]{7}\b"
hasil3 =re.findall(pattern3, artikel)
print(hasil3)
print(len(hasil3))

# 4. Ambil informasi uang
pattern4 = r'Rp .+ ribu|Rp.{3,9} juta'
hasil4 =re.findall(pattern4, artikel)
print(f'kata yang mengandung uang ada {len(hasil4)}')
print(hasil4)

#5. ganti semua kata tertentu dengan input user
kata_lama = input('masukan kata yang akan di ganti : (case sensitive): ')
kata_baru = input('masukan kata gantinya : ')
hasil5 = re.sub(kata_lama, kata_baru,artikel)

#simpan dalam file
handle = open(nama_file,'w')
handle.write(hasil5)
handle.close()


def validasi_kartu_kredit(nomor_kartu):
    if len(nomor_kartu) !=16 :
        return "tidak valid"
    elif not re.match(r"^[4-6]\d{15}$", nomor_kartu):
        return "tidak valid"
    elif re.search(r"8{4}", nomor_kartu):
        return 'Valid Platinum'
    else:
        return 'Valid Reguler'
