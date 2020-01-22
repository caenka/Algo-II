import csv

data = "nama.csv"

print("[1] Lihat Daftar")
print("[2] Buat File Baru")
print("[3] Cari Kontak")
while True:
    pilihan = input("Pilih menu")
    if (pilihan=='1'):
                contacts = []
                with open("nama.csv") as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=";")
                    for row in csv_reader:
                        contacts.append(row)
                        print(row)


    elif (pilihan=='2'):
                with open(data, mode="a") as csv_file:
                    fieldnames = ["No", "Nama", "Alamat"]
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    a = input("No urut: ")
                    b = input("Nama lengkap: ")
                    c = input("Alamat: ")

                    writer.writerow({"No": a, "Nama": b, "Alamat": c})

    elif (pilihan=='3'):
                contacts = []

                with open(data, mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        contacts.append(row)

                no = input("Inputkan nomor urut :")
                data_found = []

            # mencari contact
                indeks = 0
                for data in contacts:
                    if (data['No'] == no):
                        data_found = contacts[indeks]
                    
                    indeks = indeks + 1

                if len(data_found) > 0:
                    print("DATA DITEMUKAN: ")
                    print(f"Nama: {data_found['Nama']}")
                    print(f"Alamat: {data_found['Alamat']}")
                else:
                    print("Tidak ada data ditemukan")
    else :
                print ("Inputan yang anda masukkan salah")
                break

