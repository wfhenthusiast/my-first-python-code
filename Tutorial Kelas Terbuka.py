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
#a=10, a adalah variabel dengan nilai 10

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
#assignment secara tidak langsung, mengambil nilai dari variabel yang ada sebelumnya
b=a
print("Nilai b adalah", b)

#Tipe data
#1. tipe data: angka satuan yang tidak ada koma(integer)
data_integer = 1
print(type(data_integer))
print("data : ", data_integer, ", bertipe : ", type(data_integer))

data_integer = 100
print(type(data_integer))
print("data : ", data_integer, ", bertipe : ", type(data_integer))


print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#2. tipe data: angka dengan koma (float)
data_float = 10.3
print("data : ", data_float)
print("- bertipe :", type(data_float))

#3. tipe data: kumpulan karakter (string)
data_string = "ini siapa"
print("data : ", data_string)
print("- bertipe ", type(data_string))

#4. tipe data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool)
print("- bertipe ", type(data_bool))

## tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe ", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe ", type(data_c_double))

#casting tipe data = merubah dari satu tipe data ke tipe lain
#tipe data: int, float, str, bool

#mengubah dari data integer
print("---INTEGER---")
data_int = 2
print("data : ", data_int, ", type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0, akan true kalau nilai int > 0
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))

#mengubah dari data float
print("---FLOAT---")
data_float = 2.2
print("data : ", data_float, ", type =", type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jika nilai float = 0, akan true kalau nilai float > 0
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))

#mengubah dari data boolean
print("---BOOLEAN---")
data_bool = True
print("data : ", data_bool, ", type =", type(data_bool))

data_int = int(data_bool) #akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) #akan false jika nilai bool = 0, akan true kalau nilai bool > 0
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_float, ", type=", type(data_float))

#mengubah dari data string
print("---STRING---")
data_str = "14"
print("data : ", data_str, ", type =", type(data_str))

#jika string kosong (" "), maka tidak bisa diubah ke int dan float alias akan error
data_int = int(data_str) #string harus angka
data_float = float(data_str) #string harus angka
data_bool = bool(data_str) #akan false jika jika string kosong
print("data = ", data_int, ", type=", type(data_int))
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_bool, ", type=", type(data_bool))

print("Contoh Integer ke String")
data_int = "5/10/2021"
data_str = str(data_int)
print("Tanggal = ", data_str, "materi 06 done : ", type(data_str))

#Mengambil input data dari user
#data yang diinput akan menjadi string
data = input("Masukkan data: ")
print("data: ", data, "type = ", type(data))

#jika kita ingin mengubah input string menjadi integer, maka
data_int = int(input("Masukkan angka = "))
print("data = ",data_int,"type =",type(data_int))

#jika ingin mengubah menjadi float, maka
angka = float(input("Masukkan angka = "))
print("data = ", angka, "type = ",type(angka))

#jika ingin mengubah menjadi boolean, maka diubah terlebih dahulu menjadi integer baru ke boolean
biner = bool(int(input("Masukkan data = ")))
print("data = ", biner, "type =", type(biner))

#operasi aritmatika
#operasi penjumlahan
a = 10
b = 3
hasilnya_adalah = a + b
print(a,"+",b,"=",hasilnya_adalah)

#operasi pengurangan
hasilnya_adalah = a - b
print(a,"-",b,"=",hasilnya_adalah)

#operasi perkalian
hasilnya_adalah = a * b
print(a,"*",b,"=",hasilnya_adalah)

#operasi pembagian
hasilnya_adalah = a / b
print(a,"/",b,"=",hasilnya_adalah)

#operasi eksponen/pangkat (**)
hasilnya_adalah = a ** b
print(a,"**",b,"=",hasilnya_adalah)

#operasi modulus (%)
hasilnya_adalah = a % b
print(a,"%",b,"=",hasilnya_adalah)

#operasi floor division (//)
hasilnya_adalah = a // b
print(a,"//",b,"=",hasilnya_adalah)

#proritas operasi/ operational precedence
x = 2
y = 3
z = 4
hasil = x * z / y - (z + x) // y % x
print(x,"*",z,"/",y,"-",z,'+',x,'//',y,"%",x,"hasilnya adalah = ",hasil)
"""dalam prioritas operasi, operasi yang terkuat akan dikerjakan terlebih dahulu,
 dari yang terkuat ke yang terkecil dengan urutan dari yang terkuat yaitu
 - ()
 - eksponen
 - perkalian, pembagian, modulus, floor division
 - penjumlahan, pengurangan
 catatan: tanda kurung akan diproses paling pertama"""