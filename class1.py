num = int(input("How many numbers do you want to add"))

total = 0

for x in range(num):
      n = int(input("What is the number?::"))
      total = total + n
      print('The total at this time is',  total)
      print('_____________________________________________________________')

print('The final total is', total)
