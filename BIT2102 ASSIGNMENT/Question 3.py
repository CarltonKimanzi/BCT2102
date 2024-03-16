def sum_of_digits(number):

 sum = 0
 while number > 0:
   last_digit = number % 10
   sum += last_digit
   number //= 10
 return sum

while True:
 try:
   num_str = input("Enter a number: ")
   num = int(num_str)
   break
 except ValueError:
   print("Invalid input. Please enter a valid number.")

total_sum = sum_of_digits(num)
print("The sum of digits in", num, "is", total_sum)
