limit = 5  

print("Using for loop:")
for number in range(1, 6):  
    print(f"Multiples of {number}: ", end="")
    for multiple in range(1, limit + 1):
        print(number * multiple, end=" ")
    print()  

print("\nUsing while loop:")
number = 1
while number <= 5:
    print(f"Multiples of {number}: ", end="")
    multiple = 1
    while multiple <= limit:
        print(number * multiple, end=" ")
        multiple += 1
    print()  
    number += 1
