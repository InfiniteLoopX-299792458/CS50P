#Wouldn’t it be nice to create our own functions?

#👇🏻We can better our code to create our own special function that says “hello” for us!
# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()
# Print the output
print(f"hello, {name}")

#👇🏻We can create our own function called hello as follows:
def hello():
    print("hello")
name = input("What's your name? ")
hello()
print(name)
#Notice that everything under def hello() is indented. Python is an indented language. It uses indentation to understand what is part of the above function. Therefore, everything in the hello function must be indented. When something is not indented, it treats it as if it is not inside the hello function. Running python hello.py in the terminal window, you’ll see that your output is not exactly as you may want.

#👇🏻This time, however, you are telling the interpreter that this function takes a single parameter: a variable called to. Therefore, when you call hello(name) the computer passes name into the hello function as to. This is how we pass values into functions.
# Create our own function
def hello(to):
    print("hello,", to)
# Output using our own function
name = input("What's your name? ")
hello(name)

#👇🏻We can change our code to add a default value to hello:
# Create our own function
def hello(to="world"):
    print("hello,", to)
# Output using our own function
name = input("What's your name? ")
hello(name)
# Output without passing the expected arguments
hello()

#👇🏻We don’t have to have our function at the start of our program. We can move it down, but we need to tell the interpreter that we have a main function and a separate hello function.
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()
# Create our own function
def hello(to="world"):
    print("hello,", to)

#👇🏻The following very small modification will call the main function and restore our program to working order:
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()
# Create our own function
def hello(to="world"):
    print("hello,", to)
main()

#👇🏻EXAMPLE
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
    return n * n
main()