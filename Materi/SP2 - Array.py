#memasukkan data berkali2, jika = berhenti
a = []
b=0
while True:
    b=input("masukkan data:")
    if (b== "="):
        break #langsung keluar dari iterasi
    a.append(b)
print (a)

print ("===================")

fruits = ['mangga','pisang','jambbu']
fruits.pop() #menghapus yg terakhir
print (fruits)

print ("===================")

#menghapus data menggunakan remove dan pop menggunakan algoritma sebelumnya
a = []
b=0
while True:
    b=input("masukkan data:")
    if (b== "="):
        break
    a.append(b)
print (a)

while True:
    pilihan = input ("ingin menghapus data menggunakan :")
    if pilihan == "remove":
        remove = input ("input data yang akan dihapus:")
        a.remove(remove)
        print(a)
    elif pilihan == "pop":
        a.pop()
        print (a)
    else  :
        break

print ("===================")

#extend = menggabungkan data
#mencari data dengan menggunakan index
a = []
b=0
while True:
    b=input("masukkan data:")
    if (b== "="):
        break
    a.append(b)
print (a)

while True:
    pilihan = input ("ingin menghapus data menggunakan :")
    if pilihan == "remove":
        remove = input ("input data yang akan dihapus:")
        a.remove(remove)
        print(a)
    elif pilihan == "pop":
        a.pop()
        print (a)
    elif pilihan == "cari":
        cari = input("Data:")
        for x in range(len(a)):
            if (a[x]==cari):
               print("Data ditemukan pada index:" , x)
               break
            elif(x==(len(a)-1)):
                print ("Data tidak ditemukan")
    else  :
        break
