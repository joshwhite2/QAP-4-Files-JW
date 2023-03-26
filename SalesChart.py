#QAP 4: SALES CHART
#WRITTEN BY: JOSH WHITE
#DATE WRITTEN: MAR 22, 2023

import matplotlib.pyplot as plt

#USER INPUT
print()
print('******************************')
jan = float(input("Enter total sales for January: "))
feb = float(input("Enter total sales for February: "))
mar = float(input("Enter total sales for March: "))
apr = float(input("Enter total sales for April: "))
may = float(input("Enter total sales for May: "))
jun = float(input("Enter total sales for June: "))
jul = float(input("Enter total sales for July: "))
aug = float(input("Enter total sales for August: "))
sep = float(input("Enter total sales for September: "))
oct = float(input("Enter total sales for October: "))
nov = float(input("Enter total sales for November: "))
dec = float(input("Enter total sales for December: "))

x_axis = ["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
y_axis = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

plt.title("Monthly Sales Report")
plt.scatter(x_axis, y_axis, color = "darkred", marker = '*')
plt.grid(True)


plt.xlabel("Month")
plt.ylabel("Sales $")
plt.show()