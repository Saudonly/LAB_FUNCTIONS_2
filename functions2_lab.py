'''
Create a function that takes two parameters of type int . The function should do the following:
- Check if all the variables are negative . Else print "The numbers should be negative"
- Check that the first parameter is smaller than the second parameter .
- Using a loop Print all the numbers bettween the smaller int up to the bigger int
'''

def looping_too(num1:int, num2:int)-> list:
    for numbers in range(num1,num2+1):
        print(numbers)


while True:
   num1 = int(input("Enter the first number: "))
   num2 = int(input("Enter the second number: "))
   if num1 < 0 and num2 <0:
        if num1 < num2:
            looping_too(num1,num2)
            break
        else:
            print("The first number should be grater then the second")
   else:
        print('The numbers should be negative')




