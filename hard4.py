print("\n",15*"=","Tugas 4 hard","="*15,"\n")
# masuk perulangan dari j = 5 sampai j = 0
for j in range(5,0):
	if j == 1:
		print("There are",j,"apple on the table. A squirrel comes to eat 1 apple.")
	else:
		print("There are",j,"apples on the table. A squirrel comes to eat 1 apple.")
	berapa = int(input("How many apples are now in the table?"))
	while berapa != (j - 1):
		berapa = int(input("Salah, coba lagi: "))
# keluar perulangan saat user memasukkan angka 0

print("No apples on the table. Squirrels are full.")

print("\n",15*"=","Akhir tugas 4 hard","="*15,"\n")