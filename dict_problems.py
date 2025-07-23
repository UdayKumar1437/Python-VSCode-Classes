# arr = [10,12,13,45,55,100]
# ans = {}

# for i in arr:
#     a = []
#     for j in range(1,i+1):
#         if i%j ==0:
#             a.append(j)
#     ans[i] = a
# print(ans)

arr = [1,1,2,3,6,2]
ans= {}
for i in arr:
    ans[i] = ans.get(i,0)+1
k = ans.keys()
for i in k:
    if ans.get(i) == 1:
        print(i)