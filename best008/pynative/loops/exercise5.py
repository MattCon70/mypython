# Exercise 5: Given a list, iterate it, 
# and display numbers divisible by five, 
# and if you find a number greater than 150, stop the loop iteration.
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# Expected output:

# 15
# 55
# 75
# 150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i <= 150 and i % 5 == 0:
        print(i)
print()
print(*[i for i in list1 if i <= 150 and i % 5 == 0], sep="\n")