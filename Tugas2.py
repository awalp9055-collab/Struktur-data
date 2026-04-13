# Validasi nama
nama_benar = "awal" 
while True:
    nama = input("Masukkan nama anda: ")
    if nama == nama_benar:
        print("Nama benar, lanjut ke program berikutnya\n")
        break
    else:
        print("silahkan coba lagi\n")
angka = int(input("Masukkan angka (1-10): "))
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")