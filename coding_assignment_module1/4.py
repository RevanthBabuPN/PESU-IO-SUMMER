n = int(input("Enter the number"))
sum = 0
while (n != 0):       
    sum = sum + int(n % 10) 
    n = int(n/10) 
print("The sum of the digits is ",sum)
  

