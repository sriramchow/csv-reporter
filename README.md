# CSV Reporter

Reads a real CSV file of restaurant bills and prints a short summary report.

## Data
`tips.csv` — 15 restaurant bills (a slice of the public seaborn tips dataset).
Columns: total_bill, tip, sex, smoker, day, time, size.

## How to run
python task6.py

## What it does
- Reads each row with csv.DictReader
- Converts text numbers to real numbers with float()
- Counts the bills, totals the bills and tips, and averages them

## Results
- No of Bills: 15
- Total bill: 281.58
- Total tip: 42.41
- Average bill: 18.77
- Average tip: 2.83
