apple = 5
apple_input = input("There ore "+ str(apple) +" apples on the table. A squirrel comes to eat 1 apple. How many apples are now on the table?")
while apple > 0:
    if apple-1 == int(apple_input):#bener opo gak
        if apple-1 == 0: #ngecek terkahir
            break
        else: #uduk terahir
            apple = apple - 1 #merubah menjadi 4
            apple_input = input("There ore "+str(apple)+" apples on the table. A squirrel comes to eat 1 apple. How many apples are now on the table?")
    else: #4
        apple_input = input("Wrong, try again:")
print("No apples on the table. Squirrels are full.")