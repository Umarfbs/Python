student = {
    "name" : "Kashaf Shamim",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student)
print(student["subject"])
print(student["name"])
print(student.get("name"))
print(student["subject"]["math"])