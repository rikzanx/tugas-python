def ask(apple):
    apple_input = input("There ore "+str(apple)+" apples on the table. A squirrel comes to eat 1 apple. How many apples are now on the table?")
    check(apple,int(apple_input))
def check(apple,apple_input):
    if apple-1 == apple_input & apple-1 != 0:
        ask(apple-1)
    elif apple-1 == apple_input & apple-1 == 0:
        print("No apples on the table. Squirrels are full.")
    else:
        apple_input = input("Wrong, try again:")
        check(apple,int(apple_input))
apple = 5
ask(apple)