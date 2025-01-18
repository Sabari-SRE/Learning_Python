### print() function (Used to print the string mentioned inside).
````
print("Hello Vasuki!")
````
### String manipulation:
````
print("Hello" + " " + "Vasuki" + " " + "My Thangam!")
````
### input() function
````
print("Hello "+ input("What is your name:") + "!")
````

### Variables
````
print(len(input("What is your name?"))) --> Single line calculate the length of the input provided<br>

Calculate the length using variables
username = input("what is your name?")
length = len(username)
print(length)
````
### Switching the values between variables
````
glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
````
## Band name Generator project
````
print("Welcome to band name generator Vasuki!!!")
cityName = input("What's is the name of the city you grew up in?\n")
pet = input("What's your pet name?\n")
print("Your band name could be: " +cityName+ " " +pet)
````