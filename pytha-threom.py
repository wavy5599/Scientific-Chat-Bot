import math
import time

def polynomial():
    
    print("Let's work with polynomials!")
    response = input("Do you want to learn about polynomials? (yes/no): ").lower()

    if response == "yes":
        print("\nA polynomial is an expression made up of variables and coefficients.")
        print("For example: 3x^2 + 2x + 1\n")

        try:
            a = int(input("Enter coefficient a (for x^2 term): "))
            b = int(input("Enter coefficient b (for x term): "))
            c = int(input("Enter coefficient c (constant term): "))

            print(f"\nYour polynomial: {a}x^2 + {b}x + {c}")

        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Okay, let me know if you change your mind!")


def pytha_threom():
    print("Let's calculate the Pythagorean theorem!")
    time.sleep(1)
    print("This will only take a moment...")
    time.sleep(1)
    print("Okay, let's get started!")
    time.sleep(1)
    a = float(input("Enter the length of side a: "))
    
    b = float(input("Enter the length of side b: "))
    
    c = (a**2 + b**2)**0.5
    
    
    print(f"The length of side c is: {c}")
    
    
def foil():
    print("Let's do the FOIL method!")
    response = input("Do you want to learn the FOIL method? (yes/no): ").lower()

    if response == "yes":
        print("\nThe FOIL method is used to multiply two binomials.")
        print("For example: (a + b)(c + d) = ac + ad + bc + bd\n")

        try:
            a = int(input("Enter coefficient a (first binomial, x term): "))
            b = int(input("Enter coefficient b (first binomial, constant): "))
            c = int(input("Enter coefficient c (second binomial, x term): "))
            d = int(input("Enter coefficient d (second binomial, constant): "))

            ac = a * c
            ad = a * d
            bc = b * c
            bd = b * d

            print(f"\nYour binomials: ({a}x + {b})({c}x + {d})")
            print(f"\nFOIL steps:")
            print(f"ac = {ac}x^2")
            print(f"ad = {ad}x")
            print(f"bc = {bc}x")
            print(f"bd = {bd}")

            combined_middle = ad + bc

            print(f"\nExpanded form: {ac}x^2 + {combined_middle}x + {bd}")

        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Okay, let me know if you change your mind!")



def chat():
    greeting = "Hello there what would you like to do today?"
    print(greeting)
    response = input("Please let me know what you would like to do: \n\n")

    if response == "Lets do pythagorean theorem" or response == "Let's do py theorem" or response == "pyth theorem" or response == "Let's do pythagorean theorem!":
        print("Lets do pythagorean theorem")
        pytha_threom()
        
    elif response == "Lets do foil" or response == "Let's do foil" or response == "foil":
        print("Let's do the FOIL method!")
        foil()
    
    elif response == "Lets do polynomals" or response == "Let's do polynomials" or response == "polynomials":
        print("Let's work with polynomials!")
        polynomial()
        
    
    else:
        print("I am not sure what you mean, but I am here to help with math!")
    
    
chat()