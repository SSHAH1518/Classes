import random

correct = 0
total = 0

while total < 10:
    num1 = random.choice(range(2,12))
    num2 = random.choice(range(1,12))
    ans = num1*num2
    print("Question ", total+1)
    print(num1, " X ", num2)
    answer = int(input("Answer ="))
    if answer == ans:
        correct = correct +1
        total = total + 1
        print("CORRECT")
    else:
        total = total + 1
        print("Wrong")
    print("________________________________________________________________")

per = (correct/total)*100

print("You got ", correct , "correct.")
print(per,"%")
