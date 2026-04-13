#masukkan umur
umur = int(input("Masukkan umur anda: "))
# Percabangan kondisi
if umur < 0:
    print("anda belum lahir")
elif umur < 18:
    print("anda belum cukup umur")
elif umur > 60:
    print("banyakin ibadah, bentar lagi mati")
else:
    print("anda cukup umur")
print("Program selesai")