"""Kunal is allowed to go out with his friends only on the even days of the given month.
Write a program to count the number of days he can go out in the month of August."""

totDays = 31
days = 0
for i in range(1, totDays+1):
    if i % 2 == 0:
        days += 1
print("Kunal can go out on ", days, "days in August month!!")
