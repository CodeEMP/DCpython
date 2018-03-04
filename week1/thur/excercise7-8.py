# excercise 7
bill = int(input("Total bill amount? "))
service = input("Level of service? ")
split = int(input("Split how many ways? "))
if "good" in service:
    tip = bill * .2
elif "fair" in service:
    tip = bill * .15
elif "bad" in service:
    tip = bill * .1
print("Tip amount: ${:.2f}".format(tip))
print("Total amount : ${:.2f}".format(bill + tip))
print("Total amount per person: ${:.2f}".format((bill + tip)/split))