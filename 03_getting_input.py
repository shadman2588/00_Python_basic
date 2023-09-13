# Ask the user for their name
username = input("What's your name? ")

# Ask the user for their favourite integar
fav_num = int(input("favourite number? "))

# Double, halve and square the number
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

print()
# Greet the user
print("Hi {}, your favorite number is {}." .format(username, fav_num))
print()
# Output the results of doubling, halving, and squaring thier favourite number
print("double {} is {}" .format(fav_num, double))
print("half {} is {}" .format(fav_num, half))
print("square {} is {}." .format(fav_num, square))
print()