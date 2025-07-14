# n = 5
# # 1+2+3+4+5
# sum = 0
# for i in range(1,n+1):
#     sum = sum+i
# print(sum)


# num1 = 5
# num2 = 9
# # 5+6+7+8+9
# sum = 0
# for i in range(num1,num2+1):
#     sum=sum+i
# print(sum)

# num = 10
# for i in range(1,num+1):
#     if num%i == 0:
#         print(i)


a = [2,5,8,9,6,44,5,99]
leftHand = a[0]
for rightHand in a:
    if rightHand < leftHand:
        leftHand = rightHand
print(leftHand)