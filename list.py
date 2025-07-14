# ans = a.count(1)
# print(ans)



# a = [1,2,3,4,44,5,2,-45]
# ans = a.index(44)
# print(ans)

# a.pop(4)
# a.remove(44)
# a.insert(2,33)
# a.sort(reverse=True)
# a.reverse()
# print(a)


# num = 56
# ans = []
# for i in range(1,num+1):
#     if num%i == 0:
#         ans.append(i)
# print(ans)


# for i in range(1,6):
#     print(i,end="")
# print()
# for i in range(1,6):
#     print(i,end="")

# n = 3
# # ****
# # ****
# # ****
# # ****
# for i in range(n):
#     print("*"*n)


num  = 10
# * ->1
# ** ->2
# *** ->3
# **** ->4
# ***** ->5

for i in range(1,num+1):
    for j in range(i):
        print("*",end="")
    print()