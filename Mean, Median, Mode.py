# Write a program that calculates the mean of a list (the average of all number in the list), the Median
# (The middle number in the list) and the Mode (the most common number in the list)

# NOTE: you cannot import math and use it, you must solve these using for loops!

#list for mean, median and mode
numList = [1, 5, 8, 9, 14, 6, 2, 11, 7, 7]

#Mean(the average of all number in the list)
print(numList)
for x in numList:

    total = sum(numList)
mean = total / len(numList)
print(mean)


#Median (The middle number in the list)
numList.sort()
print(numList)
for x in numList:
    mid = (numList[4] + numList[5]) / 2
    print(mid)


#Mode (the most common number in the list)
for x in numList:
    print(numList[4], numList[5])
