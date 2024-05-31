# Welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Prompt the user for the package weight
weight = float(input("Please enter the package weight: "))

# Check if the weight is greater than 50
if weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
else:
    # Prompt the user for the package width
    width = float(input("Please enter the package width: "))
    
    # Prompt the user for the package height
    height = float(input("Please enter the package height: "))
    
    # Prompt the user for the package length
    length = float(input("Please enter the package length: "))
    
    # Check if the sum of dimensions is greater than 50
    if (width + height + length) > 50:
        print("Package too big to be shipped via Package Express.")
    else:
        # Calculate the shipping quote
        quote = (width * height * length * weight) / 100
        
        # Display the shipping quote to the user
        print(f"Your estimated total for shipping this package is: ${quote:.2f}")
        print("Thank you!")
