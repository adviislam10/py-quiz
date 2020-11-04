# Questions
Q1 = input("What ocean is on the eastern coast of Canada?  ").lower()
A1 = Q1

Q2 = input("What is the national bird of the United States?  ").lower()
A2 = Q2

Q3 = input("In which country did the ancient Mayans live in?  ").lower()
A3 = Q3

Q4 = input("What animal lays eggs that turn into tadpoles?").lower()
A4 = Q4

# Answers and Score
x = 0

if A1 == "atlantic":
    print("Q1 CORRECT")
    x = x + 1
elif A1 == "atlantic ocean":
    print("Q1 CORRECT")
    x = x + 1
else:
    print("Q1 INCORRECT")

if A2 == "bald eagle":
    print("Q2 CORRECT")
    x = x + 1
elif A2 == "the bald eagle":
    print("Q2 CORRECT")
    x = x + 1
else:
    print("Q2 INCORRECT")

if A3 == "mexico":
    print("Q3 CORRECT")
    x = x + 1
else:
    print("Q3 INCORRECT")

if A4 == "frog":
    print("Q4 CORRECT")
    x = x + 1
elif A4 == "frogs":
    print("Q4 CORRECT")
    x = x + 1
else:
    print("Q4 INCORRECT")

print(x, "/4 " , x/4, "%")