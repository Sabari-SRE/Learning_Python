print("Welcome to BMI calculator!!")
weight=int((input("Enter your weight: ")))
height=float((input("Enter your Height: ")))
bmi=weight/height**2
final_bmi=round(bmi, 2)
print(f"your bmi is: {final_bmi}")