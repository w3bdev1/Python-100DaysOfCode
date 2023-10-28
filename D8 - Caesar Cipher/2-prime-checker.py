n = int(input("Give me a number: "))

def prime_checker(num):
    for n in range(2, num):
        if num%n == 0:
            print("It's not a prime number")
            return
    
    print("It's a prime number")

prime_checker(n)