# Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello,", name)

# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print('hello, \'friend\'')

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str (to remove the extra spaces that is entered by mistake)
name = name.strip()

# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")

# Notice the f in print(f"hello, {name}").
# This f is a special indicator for Python to treat this string a special way
# This f string is a more often used these days.

# 👇🏻 By utilizing the strip method on name (for example, name = name.strip()), you will remove any whitespace from the left and right of the user’s input. You can modify your code to be:
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")