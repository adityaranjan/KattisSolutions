numbers = input()
x,y,n = numbers.split(" ")
for i in range(int(n)):
    if (((i+1) % int(x)) == 0) and (((i+1) % int(y)) == 0):
        print("FizzBuzz")
    elif (((i+1) % int(x)) == 0) and (((i+1) % int(y)) != 0):
        print("Fizz")
    elif (((i+1) % int(x)) != 0) and (((i+1) % int(y)) == 0):
        print("Buzz")
    else:
        print(str(i+1))
        