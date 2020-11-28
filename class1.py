num = int(input("How many numbers do you want to add::"))

total = 0

for x in range(num):
    n = int(input("What is the number?::"))
    total += n
    print("The total right now is ", total)
    print("____________________________________________________________________")

print("The final total is ", total)
