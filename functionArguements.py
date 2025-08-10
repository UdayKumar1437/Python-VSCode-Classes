# Function Arguements and return statement

# There are four types of arguements that we can provide in a function
# Default Arguement
# Keyword Arguement
# Variable length Arguement
# Required Arguement


# Default Arguement
# def name(fName,lName="Sheik"):
#     print(fName+" "+lName)

# name("Rizwana")

# Keyword Arguement
# def name(fName,friend,lName):
#     print(fName+" "+lName+" "+friend)

# name(fName="Sheik",lName="Rizwana",friend="Uday")

# Required Arguement
# def name(fName,lName):
#     print(fName+" "+lName)

# name("Rizwana")

# Variable Length Arguement

# Arbitrary Arguement
# def add(*nums):
#     sum = 0
#     for i in nums:
#         sum+=i
#     print(sum)

# add(1)


# Keyword Arbitrary Arguement

# def name(**names):
#     print(names)

# name(fname="Sheik",lName="Rizwana")


# Return Statement
# def add(a,b):
#     print( a+b)

# ans = add(1,2)
# print(ans)