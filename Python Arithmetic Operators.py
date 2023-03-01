#Python Arithmetic Operators
#Additon (penjumlahan)
x=10
y=3
hasil = x+y
print(hasil)

#Subtraction
hasil = x-y
print(hasil)

#Multiplication
hasil = x*y
print(hasil)

#Division
hasil = x/y
print(hasil)

#Modulus
hasil = x%y
print(hasil)

#Exponentiation
#sama seperti x dipangkatkan sebanyak y
hasil = x ** y
print(hasil)

#Floor Division
hasil = x // y
print(hasil)

#Tipe Data
#list
daftar_siswa = [
    "tono",
    "supri",
    "susana",
    "siapa"
]
print(daftar_siswa)

#slicing index
#tanda koma dalam list menandakan index atau nomor urut yang dimulai dari 0
print(daftar_siswa[:3])

#tipe data mapping (array asosiatif)
daftar_siswa = {
    "1": "luhut",
    "2": "binsar",
    "3": "panjaitan",
    "4": "riki",
    "5": "faisal"
}

for angka, siswa in daftar_siswa.items() :
    print(f"angka: {angka} nama: {siswa}")
print(daftar_siswa['3'])


nama_kota = {
    "1": "medan",
    "2": "surabaya",
    "3": "jogja",
    "4": "maluku",
    "5": "sidrap"
}

for nomor, kota in nama_kota.items() :
    print(f"nomor: {nomor} kota: {kota}")

from ctypes import c_double