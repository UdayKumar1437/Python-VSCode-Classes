myData = {
    "name":"Uday Kumar",
    "age":25,
    "Gender":"M"
}

# print(myData.items())

# for i in myData.keys():
#     print(i)


myData["isGraduated"] = True
print(myData.get("Genderone","Not Applicable"))
# myData.popitem()
myData.pop("age")

myData.update({
    "student1":"Kedar",
    "student2":"Rizwana",
    "ages":[18,18]
})
print(myData)