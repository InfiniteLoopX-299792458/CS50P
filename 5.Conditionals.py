# >= denotes “greater than or equal to.”
# <= denotes “less than or equal to.”
# == denotes “equals.” Note the double equal sign: a single equal sign assigns a value, whereas two equal signs compare values.
# != denotes “not equal to.”

x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")

x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
#👆🏻
# =============================================================================
#
#                               START
#                                 |
#                                 |
#                              ┌───────┐
#                              │ x < y │
#                              └───┬───┘
#                             True│   │False
#                                 │   │
#                                 │   ────────────────┐
#                                 │                   │
#                                 ▼                   |
#                     ┌───────────────────────┐       |
#                     │ "x is less than y"    │       |
#                     └──────────┬────────────┘       |
#                                │                    | 
#                                ▼                    |
#                            ┌───────┐                |
#                            │ x > y │◄───────────────┘
#                            └───┬───┘                
#                           True│   │False           
#                               │   │               
#                               ▼    ───────────────┐          
#                  ┌────────────────────────┐       |
#                  │ "x is greater than y"  │       |
#                  └──────────┬─────────────┘       |
#                             │                     │
#                             ▼                     │
#                         ┌────────┐◄───────────────┘
#                         │ x == y │
#                         └───┬────┘
#                        True│   │False
#                            │   │
#                            ▼   ────────────────┐
#              ┌────────────────────────┐        |
#              │ "x is equal to y"      │        |
#              └──────────┬─────────────┘        |
#                         │                      |
#                         ▼                      |
#                        STOP◄───────────────────┘
#
# =============================================================================

#👇🏻 First, the if statement is evaluated. If this statement is found to be true, all the elif statements will not be run at all. However, if the if statement is evaluated and found to be false, the first elif will be evaluated. If this is true, it will not run the final evaluation.
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
# =============================================================================
#                           FLOWCHART
# =============================================================================
#
#        Start                              
#          │
#          ▼
#        ◇ x < y ◇
#       ╱         ╲
#     True      False
#      │            ╲
#      │             ╲
#      │              ◇ x > y ◇
#      │             ╱         ╲
#      │          True       False
#      │            │            ╲
#      ▼            │             ◇ x == y ◇
# ┌──────────┐       │           ╱         ╲
# │ x<y      │       ▼        True        False
# └────┬─────┘  ┌──────────┐    │           ╲
#      │        │ x>y      │    ▼            ╲
#      │        └────┬─────┘ ┌──────────┐     ╲
#      ╲             │       │ x==y     │      ╲
#       ╲            │       └────┬─────┘       ╲
#        ╲___________│____________│______________╱
#                    ▼
#                   stop
#
# =================================================================

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
#👆🏻
# =============================================================================
#
#                                  start
#                                    │
#                                    ▼
#                               ╱─────────╲
#                              ╱   x < y   ╲
#                              ╲           ╱
#                               ╲─────────╱
#                              ╱           ╲
#                    True     ╱             ╲ False
#                            ╱               ╲
#                           ╱                 ▼
#                          ╱             ╱─────────╲
#                         ╱             ╱   x > y   ╲
#                        ╱              ╲           ╱
#                       ╱                ╲─────────╱
#                      │                ╱         ╲
#                      │          True ╱           ╲ False
#                      │              ╱             ╲
#                      ▼             ▼               ▼
#         ┌────────────────────┐ ┌────────────────────┐ ┌───────────────────┐
#         │ "x is less than y" │ │"x is greater than y"│ │ "x is equal to y" │
#         └──────────┬─────────┘ └──────────┬─────────┘ └──────────┬────────┘
#                    ╲                      │                      ╱
#                     ╲                     │                     ╱
#                      ╲                    ▼                    ╱
#                       ╲               ╭────────╮              ╱
#                        ╲─────────────▶│  stop  │◀────────────╱
#                                       ╰────────╯
#
# =============================================================================

#👇🏻"or" allows your program to decide between one or more alternatives. For example, we could further edit our program as follows:
x = int(input("What's x? "))
y = int(input("What's y? "))
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
#👆🏻Notice that the result of our program is the same, but the complexity is decreased. The efficiency of our code is increased.

#👇🏻Notice how we removed the or entirely and simply asked, “Is x not equal to y?” We ask one and only one question. Very efficient!
x = int(input("What's x? "))
y = int(input("What's y? "))
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#👇🏻Notice that the == operator evaluates if what is on the left and right are equal to one another.
x = int(input("What's x? "))
y = int(input("What's y? "))
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
#👆🏻
# =============================================================================
#
#                                  start
#                                    │
#                                    ▼
#                              ╱───────────╲
#                             ╱   x == y    ╲
#                             ╲             ╱
#                              ╲───────────╱
#                               ╱         ╲
#                       True   ╱           ╲   False
#                             ╱             ╲
#                            ▼               ▼
#                ┌───────────────────┐   ┌───────────────────────┐
#                │ "x is equal to y" │   │ "x is not equal to y" │
#                └─────────┬─────────┘   └───────────┬───────────┘
#                          ╲                         ╱
#                           ╲                       ╱
#                            ╲                     ╱
#                             ╲     ╭────────╮    ╱
#                              └───▶│  stop  │◀──┘
#                                   ╰────────╯
#
# =============================================================================

#👇🏻Similar to or, and can be used within conditional statements.
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >=80 and score < 90:
    print("Grade: B")
elif score >=70 and score < 80:
    print("Grade: C")
elif score >=60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#👇🏻We could improve our code as follows:
score = int(input("Score: "))
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
    
#👇🏻Can you improve the code further?, yes, like this:
score = int(input("Score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#👇🏻The modulo "%" operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.
#For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenly and would result in a number other than zero!
x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#👇🏻Notice that our if statement is_even(x) works even though there is no operator there. This is because our function returns a bool (Boolean), True or False, back to the main function. The if statement simply evaluates whether or not is_even of x is true or false.
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()

#👇🏻Much simpler and improved version
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return True if n % 2 == 0 else False
main()

#👇🏻Even more improved version
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return n % 2 == 0
main()
#👆🏻The program will evaluate what is happening within the n % 2 == 0 as either True or False and simply return that to the main function.

#⭐ MATCH
#Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.
name = input("What's your name? ")
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#👇🏻We can improve this code slightly with the use of the "or" keyword:
name = input("What's your name? ")
if name == "Harry" or name == "Hermione" or name == "Ron": 
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#👇🏻Alternatively, we can use match statements to map names to houses. Consider the following code:
name = input("What's your name? ")
match name: 
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
#👆🏻Notice the use of the "_" symbol in the last case. This will match with any input, resulting in similar behavior as an else statement.

#👇🏻We can improve the code:
name = input("What's your name? ")
match name: 
    case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
    case "Draco":
          print("Slytherin")
    case _:
          print("Who?")
#👆🏻Notice, the use of the single vertical bar |. Much like the or keyword, this allows us to check for multiple values in the same case statement.
