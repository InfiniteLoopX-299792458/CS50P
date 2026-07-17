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

#Notice that we’ve introduced two new keywords in Python, continue and break. continue explicitly tells Python to go to the next iteration of a loop. break, on the other hand, tells Python to “break out” of a loop early before it has finished all of its iterations. In this case, we’ll continue to the next iteration of the loop when n is less than 0—ultimately reprompting the user with “What’s n?”. If, though, n is greater than or equal to 0, we’ll break out of the loop and allow the rest of our program to run.
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

#It turns out that the continue keyword is redundant in this case. We can improve our code as follows:
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
#Notice how this while loop will always run (forever) until n is greater than 0. When n is greater than 0, the loop breaks.

#Notice how not only did we change your code to operate in multiple functions, but we also used a return statement to return the value of n back to the main function.
def main():
    meow(get_number())
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")
main()

#Notice how we have a list of students with their names as above. We then print the student who is at the 0th location, “Hermione”. Each of the other students is printed as well.
students = ["Hermione", "Harry", "Ron"]
print(students[0])
print(students[1])
print(students[2])

#Notice that for each student in the students list, it will print the student as intended. You might wonder why we did not use the _ designation as discussed prior. We choose not to do this because student is explicitly used in our code.
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(student)

#-------------------------------------------------*****-----------------------------------------------
#-------------------------------------
#               LENGTH
#-------------------------------------
#Imagine that you don’t simply want to print the name of the student but also their position in the list. To accomplish this, you can edit your code as follows:
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])
#Notice how executing this code results in not only getting the position of each student plus one using i + 1, but also prints the name of each student. len allows you to dynamically see how long the list of the students is regardless of how much it grows.
#-------------------------------------------------*****-----------------------------------------------

#dicts or dictionaries are a data structure that allows you to associate keys with values.
#Where a list is a list of multiple values, a dict associates a key with a value.

#The individual at the first position of students is associated with the house at the first position of the houses list, and so on.
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

#use {} curly braces to create a dictionary. Where lists use numbers to iterate through the list, dicts allow us to use words.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#students[student] will go to each student’s key and find the value of their house. Execute your code, and you’ll notice how the output is a bit messy.
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student])

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")
#👇🏻
#$ python hogwarts.py
#Hermione, Gryffindor
#Harry, Gryffindor
#Ron, Gryffindor
#Draco, Slytherin

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

#👇🏻

#Hermione, Gryffindor, Otter
#Harry, Gryffindor, Stag
#Ron, Gryffindor, Jack Russell terrier
#Draco, Slytherin, None

#the for loop will iterate through each of the dicts inside the list called students.
#this code creates a list of dicts. The list called students has four dicts within it: One for each student. Also, notice that Python has a special None designation where there is no value associated with a key.

#-----Mario-----
#emember that the classic game Mario has a hero jumping over bricks. Let’s create a textual representation of this game.

#Notice how we are copying and pasting the same code over and over again.
print("#")
print("#")
print("#")

# or 👇🏻

for _ in range(3):
    print("#")

# column can grow as much as we want without any hard coding.
def main():
    print_column(3)
def print_column(height):
    for _ in range(height):
        print("#")
main()

#Now, let’s try to print a row horizontally. Modify your code as follows:
def main():
    print_row(4)
def print_row(width):
    print("?" * width)
main()

#
