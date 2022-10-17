from flat import Bill, Flatmate
from reports import PdfReport
import os


amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? e.g December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))




total_bill = Bill(amount, period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} Pays: ", flatmate1.pays(total_bill, flatmate2))
print(f"{flatmate2.name} Pays: ", flatmate2.pays(total_bill, flatmate1))

pdf_report = PdfReport(filename=f"{total_bill}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=total_bill)