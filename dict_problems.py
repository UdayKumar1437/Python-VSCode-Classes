# arr = [10,12,13,45,55,100]
# ans = {}

# for i in arr:
#     a = []
#     for j in range(1,i+1):
#         if i%j ==0:
#             a.append(j)
#     ans[i] = a
# print(ans)

# arr = [1,1,2,3,6,2]
# ans= {}
# for i in arr:
#     ans[i] = ans.get(i,0)+1
# k = ans.keys()
# for i in k:
#     if ans.get(i) == 1:
#         print(i)


# def isPrime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count == 2:
#         return True
#     else:
#         return False


# start = 10
# end =1000
# ans =[]
# for i in range(start,end+1):
#     if isPrime(i):
#         ans.append(i)
# print(ans)

# def factors(num):
#     ans = []
#     for i in range(1,num+1):
#         if num%i ==0:
#             ans.append(i)
#     return ans

# num = 100
# factorsOfNum = factors(num)
# ans = []
# for i in factorsOfNum:
#     if isPrime(i):
#         ans.append(i)
# print(ans)


# Break and Continue

#Break --> It will terminate the loop asap
# Continue --> It will skip the current iteration
# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)
# print("Done")



# 5 * 1 = 5
# 5*2 = 10



# 5*20 = 100