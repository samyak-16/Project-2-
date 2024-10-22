import random
n = random.randint(1,100)
counter = []
a= None
while (a != n ):
    a = int(input("Guess a number between  (1 - 100 ) \n " ))

    if a>n :
        print("Lower please !!")
    elif a<n :
        print("Greter Please!!")
    counter.append(a)

print(f"You guessed it in  {len(counter)} tries   . ")
# fastest way - '''https://chatgpt.com/c/6704f6e4-822c-800b-af25-f2102f86d905'''




