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
# x = int(input("What's x? "))
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
