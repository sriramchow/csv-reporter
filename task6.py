import csv

total_bill = 0
total_tip = 0
count = 0

with open("tips.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_bill = total_bill + float(row["total_bill"])
        total_tip = total_tip + float(row["tip"])
        count = count + 1

print(f"Total bill: {total_bill}")
print(f"Total tip: {round(total_tip,2)}")
print(f"No of Bills: {count}")
print(f"Average bill: {round(total_bill/count, 2)}")
print(f"Average tip: {round(total_tip/count, 2)}")
