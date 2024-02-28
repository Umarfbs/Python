#strings is data type that stores a sequence of characters
#length of string len(str)

str1= "Kashaf"      #is se hum apne string ki length jaan sakte hain
print(len(str1))
print(type(str1))
str2= "Shamim"
len2=len(str2)
print(len2)
#print(len(str2))
final_str= str1+" " +str2
print(final_str, len(final_str))

#Indexing  index > position
#apna_college
#01234567891011
# str="apna_college"
# str[0] is 'a', str[1] is 'p' ...
# str[0] ='b' # not allowed

string= "Kashaf Bin Shamim"     #is se hum apne character ki position jaan sakte hain
character= string[3]
print(character)

st1 = " hello world"        # is se hum shortcut mein character ki position jaan sakte hain
print(st1[5])


#slicing : accessing parts of a string
#str[starting_index:ending_inddex]

a="kashaf shamim"
print(a[1:4])
print(a[7:])
print(a[:7])
print(a[-6:-1]) #Negative Slicing