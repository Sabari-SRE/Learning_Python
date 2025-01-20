### Datatypes
Primitive datatypes (string,integer,float,boolean)

#### subscripting
````
print("Hello!"[0]) --> To print the value of the 0 position in the string
print("Hello!"[-1]) --> Same like above but take from backwards
````
#### Type checking and conversion
Examples to check the type
````
len("Vasuki")
print(type("Vasuki"))
print(type(123))
print(type(143.23))
print(type(True))
````
Example of type conversion str(),int(),float()
````
print("Number of letters in your name: " + str(len(input("Enter your name"))))
````
### Mathematical operations
Learn about the basic operators(=,-,*,/,//,**) and BODMAS
Examples:
````
print("My age: " + str(12))
print(3 * 3 + 3 / 3 - 3) --> Answer is 7
print(int(3 * (3 + 3) / 3 - 3)) --> Answer is 3
````
### Number Manipulation
round() --> Function to round the decimal number <br>
Syntax: round(value, digit)

Assignment Operators (+=,-=,*=,/=)

f-Strings
In Python, we can use f-strings to insert a variable or an expression into a string.
````
age = 12
print(f"I am {age} years old")
````

### BMI calculator
````
weight=(input("Enter your weight: ")
height=(input("Enter your Height: ")
bmi=weight/height**2
final_bmi=round(bmi, 2)
print(f"your bmi is: {final_bmi}")