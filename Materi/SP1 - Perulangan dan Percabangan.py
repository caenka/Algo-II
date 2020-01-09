A = True
B = False
if not A:
    print ("A")
else :
    print ("B")
#####

import random

loop = True
while loop :

    cowok = input ("Masukan nama cowok : ")
    cewek = input ("Masukan nama cewek :")
    print ("===================")
    print ("Nama cowok :" ,cowok)
    print ("Nama cewek :", cewek)

    confirm = input ("Apakah nama yang dimasukkan sudah benar? y/n:")
    if confirm=='y':
            loop = False;  ## kenapa tidak pakai Else karena tidak memenuhi untuk loop=false,
 # var loop akan tetap true
match = random.randrange(0,100)
print('Match', match, '%')
if match > 80 :
    print ("ndang rabi")
elif match >60 :
    print ("pikir-pikir")
elif match >40 :
    print ("yakin ?")
elif match >20:
    print ("cari lagi")
else :
    print ("putus aja")
