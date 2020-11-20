print("\n",15*"=","Tugas 4 easy","="*15,"\n")
angka = 0

# masuk perulangan
while angka >= 0:
	try:
		angka = int(input("Masukkan angka: "))
		if angka == 7:
			print("DOOORRR!!!")     # akan dieksekusi jika angka = 7
	except:
		print("input yang dimasukkan bukan angka!")
# keluar perulangan, saat variabel angka bernilai negatif

print("\n",15*"=","Akhir tugas 4 easy","="*15,"\n")