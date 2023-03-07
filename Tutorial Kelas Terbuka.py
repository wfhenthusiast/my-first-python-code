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

data_int = 2
print("data : ", data_int, ", type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0, akan true kalau nilai int > 0
print("data = ", data_float, ", type=", type(data_float))
print("data = ", data_str, ", type=", type(data_str))
print("data = ", data_bool, ", type=", type(data_bool))
