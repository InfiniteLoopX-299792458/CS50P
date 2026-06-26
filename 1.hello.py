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
# Think of it like this:
# "..." → normal string
# f"..." → string with live variables/calculations inside {}

# 👇🏻 By utilizing the strip method on name (for example, name = name.strip()), you will remove any whitespace from the left and right of the user’s input. You can modify your code to be:
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")


#👇🏻Using the title method, it would title case the user’s name: [even if u enter it in lowercase, will automatically capitalize the first letter of each word]
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Print the output
print(f"hello, {name}")


#👇🏻More efficient:
name = input("What's your name? ").strip().title()
print(f"hello, {name}")

#or

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"hello, {name}")