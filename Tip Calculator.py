print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#solution 2
bill_amount = (tip / 100 * bill + bill)
Split_amount =(bill_amount/people)
bill_per_person = round(Split_amount, 2)
print(f"Each person should pay {bill_per_person}")

#solution 1
tip_percentage = tip/100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_each_person = total_bill / people
final_amount= round(bill_each_person, 2)
print(f"Each person should pay {final_amount}")