import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#Option 1
random_person_to_pay_bill=random.choice(friends)
print(random_person_to_pay_bill)

#Option 2
random_person_index=random.randint(0,4)
print(friends[random_person_index])