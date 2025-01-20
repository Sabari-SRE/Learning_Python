## Randomisation and lists in python

### Random module <br> 
**To generate pseudo random generated numbers(i,e computer generated numbers)**
Reference document : https://docs.python.org/3/library/random.html
````
import ramdom --> 
sample functions : random.randint, random.choice
````
### Coin flip program
````
import random
random_number=random.randint(0,1)
print(random_number)
if random_number == 0:
    print("Heads")
else:
    print("Tails")
````
### Lists (Very important topic) (Refer list.py)
#### Sample code
````
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[3])
states_of_america[3]="Phoenix"
print(states_of_america)
states_of_america.append("SabariVasuki land")
print(states_of_america)
states_of_america.extend(["abc","def"])
print(states_of_america)
````
### Banker Roulette (Refer BankerRoulette.py)
### IndexError (Refer DirtyDozen.py)
Reference document : https://docs.python.org/3/library/functions.html#len

### Rock paper scissors project (Refer Rock Paper Scissors.py)