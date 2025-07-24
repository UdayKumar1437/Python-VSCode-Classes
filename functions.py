# num =32
# ans = []
# for i in range(1,num+1):
#     if num%i ==0:
#         ans.append(i)
# print(ans)


# num2 =27
# ans2 = []
# for i in range(1,num2+1):
#     if num2%i ==0:
#         ans2.append(i)
# print(ans2)


# def name():
#     print("Rizwana")
#     print("Kedar")
#     for i in range(5):
#         print("Uday")
# def rizwana():
#     print("Rizwana from Rizwana Function")
# for i in range(10):
#     name()
# rizwana()



# def Factors(kedarNum):
#     ans = []
#     for i in range(1,kedarNum+1):
#         if kedarNum%i ==0:
#             ans.append(i)
#     print(ans)


# Factors(10)
# Factors(25)
# Factors(1546898)



# def isPrime(num):#10
#     count = 0
#     for i in range(1,num+1):
#         if num%i ==0:
#             count+=1

#     if count == 2:
#         print("Prime")
#     else:
#         print("Not a prime")

# isPrime(10)
# isPrime(7)



def greet(name):
    print("Good Morning",name)

# greet("Rizwana")

def isPalindromeString(stringName):
    if stringName == stringName[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
isPalindromeString()