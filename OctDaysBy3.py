#Write a program to count the number of days in October (31 days) that are divisible by 3.
totDays = 31
days = 0
for i in range(1, totDays+1):
    if i % 3 == 0:
        days += 1
print("There are  ", days, "days in October month that are divisible by 3!!!")
