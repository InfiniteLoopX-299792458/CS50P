x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

#👇🏻The output will be rounded to the nearest integer.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Create a rounded result
z = round(x + y)
# Print the result
print(z)

#👇🏻Though quite cryptic, that print(f"{z:,}") creates a scenario where the outputted z will include commas where the result could look like 1,000 or 2,500.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Create a rounded result
z = round(x + y)
# Print the formatted result
print(f"{z:,}")

#👇🏻As we might expect, this will round the result to the nearest two decimal points.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the result and round
z = round(x / y, 2)
# Print the result
print(z)

#👇🏻This cryptic f-string code displays the same as our prior rounding strategy.
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))
# Calculate the result
z = x / y
# Print the result
print(f"{z:.2f}")