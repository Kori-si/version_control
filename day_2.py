# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
number = int(two_digit_number)

number_1 = number//10
number_2 = number%10

digit = number_1 + number_2

print(digit)
