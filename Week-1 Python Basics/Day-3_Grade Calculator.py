g=int(input("Enter your grade: "))

if g >= 90:
    print("You got an A")
    print("Excellent work!")
elif g >= 80:
    print("You got a B")
    print("Good job!")
elif g >= 70:
    print("You got a C")
    print("You did well.")
elif g >= 60:
    print("You got a D")
    print("You need to improve.")
elif g >= 50:
    print("You got an E")
    print("You need to work harder.")
elif g < 50:
    print("You got an F")
    print("You need to retake the course.")
else:
    print("Invalid grade. Please enter a valid grade between 0 and 100.")

print("\nThank you for using the grade calculator!\n")