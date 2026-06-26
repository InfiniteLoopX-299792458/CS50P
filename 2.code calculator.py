x = 1
y = 2
z = x + y
print(z)

# 👇🏻if u enter x = 1 and y = 2, z will be "12" (string concatenation) [which is not the desired behavior]
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z)

# 👇🏻Prior, we have seen how the + sign concatenates two strings. 
# 👇🏻Because your input from your keyboard on your computer comes into the interpreter as text, it is treated as a string. 
# 👇🏻We, therefore, need to convert this input from a string to an integer. We can do so as follows:
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)