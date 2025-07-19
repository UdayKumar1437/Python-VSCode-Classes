# n = 154
# l = len(str(n))
# sum = 0
# for i in str(n):
#     sum = sum +int(i)**l
# if(n == sum):
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong number")


#Fibonecci

# n = 10
# a =0
# b =1
# print(a,b,end=" ")
# for i in range(n-2):
#     c= a+b
#     print(c,end=" ")
#     a = b
#     b =c


# n = 5
# exp = 3
# print(n**exp)


n = 120
sum = 0
for i in str(n):
    sum += int(i)
if n%sum ==0:
    print("Harshad Number")
else:
    print("Not an Harshad Number")