#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator!")
bill= input("What was the total bill?:")
tip = input("How much tip would you like to give? 0, 12, or 15?")
person = input("How many people to split the bill?")

pay = (float(bill)+(float(bill)*(int(tip)/100)))/int(person)

son= (round(pay,2))
print(f"Each person should pay: {son} $")