print("Hello World")
print("Tes")
print("apa")

print("oke")

#ini adalah comment sebaris
"""
ini adalah comment multiline
"""
a=11
print(a)
"""
kita bisa mengcompile python ke yang namanya bytecode dengan cara buka terminal dan 
tuliskan python -m py_compile Main.py (nama file)
"""

#variabel, adalah tempat menyimpan data

#assignment nilai
#di python tidak perlu deklarasi variabel
a=10
x=20
lebar=30
#pemanggilan pertama
print("lebarnya adalah", lebar)
print("Nilai a adalah", a)

#penamaan
nilai_y = 20
#penamaan dua variabel tidak boleh menggunakan spasi tapi boleh menggunakan _
#variabel tidak boleh diawali dengan angka

#pemanggilan kedua
print("Nilai a adalah", a)
print("lebarnya adalah", lebar)
a=20
print("Nilai a adalah", a)

#assignment indirect
b=a
print("Nilai b adalah", b)
