i = 3
while i != 0:
  print("meow")
  i = i - 1

#We can further improve our code as follows:
#notice how i += 1 is the same as saying i = i + 1.
i = 1
while i <= 3:
      print("meow")
      i = i + 1

# Now lets talk about for loops.
# For loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
for _ in range(3):
    print("meow")
#Notice how range(3) provides back three values (0, 1, and 2) automatically. This code will execute and produce the intended effect, meowing three times.
#Changing i into _ is a common practice when the variable is not going to be used in the loop. It is a way to indicate that the variable is intentionally being ignored.

print("meow" * 3)
#Notice how it will meow three times, but the program will produce "meowmeowmeow" as the result. Consider: How could you create a line break at the end of each meow?

print("meow\n" * 3, end="")
#The \n character is a newline character, which creates a line break.
# By multiplying "meow\n" by 3, we get three lines of "meow".
# The end="" argument in the print function prevents an additional newline from being added at the end of the output.
