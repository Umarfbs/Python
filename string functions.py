#The endswith() method 
#returns True if the string ends with the specified value, otherwise False
a="My name is kashaf"
print(a.endswith("haf"))

#str.capitalize() 
#captalises 1st character
b="my name is kashaf"
print(b.capitalize())
print(b)

# c = "my name is kbs"  
#captalise original string
# c=c.capitalize()
# print(c)

#replace string
#str.replace(old,new) replaces all occurences of old
d="my name is azhar"
print(d.replace("a","b"))
print(d.replace("azhar", "arshad"))

#Find String
#returns 1st index of 1st occurrer
e="my name is azhar"
print(e.find("name"))

#Count String
#Counts the occurence of substr
f="my name is is azhar"
print(f.count("is"))