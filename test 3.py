n = int(input("Enter: "))
a = []
for i in range(n):
    num = int(input("Enter an integer: "))
    a.append(num)
print(a)    
#largest_num = max(a)
#print("The largest number:", largest_num)

gtmax = a[0]

for i in a:
    if gtmax < i :
        gtmax = i

print("The largest number:", gtmax)

gtmin = a[0]

for i in a:
    if gtmin > i :
        gtmin = i

print("The smallest number:", gtmin)