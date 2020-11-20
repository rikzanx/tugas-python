total = 0
angka_input = input("Enter the numbers:")
if int(angka_input) <= 100:
    total = total + int(angka_input)
angka_input = input("Enter the numbers agains:")
if int(angka_input) <= 100:
    total = total + int(angka_input)
cek = input("would you like to enter numbers agains:")

while cek == "yes":
    angka_input = input("Enter the numbers agains:")
    if int(angka_input) <= 100:
        total = total + int(angka_input)
    cek = input("would you like to enter numbers agains:")

print("YOur total number is "+ str(total))