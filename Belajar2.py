import math

print(">>>Mencari luas dan keliling lingkaran<<<")

print("1.Keliling Lingkaran")
print("2.Luas lingkaran")

pilihan = int(input("Masukkan pilihan anda (1/2):"))

Jari_Jari =float(input("Masukkan jari-jari lingkaran :"))

if pilihan == 1 :
    keliling = 2 * math.pi * Jari_Jari
    print("Keliling lingkaran =" , round(keliling, 2))

elif pilihan == 2 :
    luas = math.pi * Jari_Jari ** 2
    print("Luas lingkaran =" , round(luas, 2))

else:
    print("Disuruh milih 1 atau 2 malah ngelunjak , ya ngak keluar hasilnya!!!")