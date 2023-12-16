
import math

#tambah
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)

#kurang
def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)

#kali
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)

#bagi
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil bagi dari",bil1,"/",bil2,"=",hasil)

#Pangkat
def Pangkat(angka1,angka2):
    hasil = (angka1 ** angka2)
    print("Hasil Pangkat dari",angka1,"**",angka2,"=",hasil)


#Sin
def Sin(bil):
    print ('Sin dari',bil,'adalah',math.sin(bil))

#Cos
def Cos(bil):
    print ('Cos dari',bil,'adalah',math.cos(bil))

#Tan
def Tan(bil):
    print ('Tan dari',bil,'adalah',math.tan(bil))

#Log
def Log(bil):
    print ('Log dari',bil,'adalah',math.log(bil))

#Akar
def Akar(bil):
    print ('Akar dari',bil,'adalah',math.sqrt(bil))


