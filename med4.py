print("\n",15*"=","Tugas 4 medium","="*15,"\n")
lagi, angka, jumlah = "", 0, 0

# masuk perulangan
while lagi != "hmmm":
	
	# masuk pengujian
	try:
		angka = int(input("Masukkan angka: "))
	except:
		# akan dieksekusi jika input bukan berupa angka
		print("input yang dimasukkan bukan angka!")
		# mengembalikan angka ke 0 agar tidak menambah jumlah
		angka = 0
	# keluar pengujian
	
	# menambahkan angka di bawah 100 ke jumlah
	if angka < 100:
		jumlah += angka             
	lagi = input("Ingin memasukkan angka lagi?")
# keluar perulangan, saat variabel lagi bernilai 'hmmm'

print("\nTotal angka yang telah dimasukkan: ",jumlah)

print("\n",15*"=","Akhir tugas 4 medium","="*15,"\n")