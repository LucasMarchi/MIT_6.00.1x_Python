#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2

s = "azcbobobegghakl"

i = 0 # variable used to know the position of the "c" variable in "s"
temp = "" # variable to caught the substring of s, starting from i
count = 0 # variable to count how many times bob appears

for c in s:    
    if c == "b":
        temp = s[i:] # set temp to "b......."
        if len(temp) >= 3: # this validation prevents the "array out of index" problem           
            if "bob" == temp[0:3]: # check first 3 characteres of temp is equal "bob"
                count += 1 # increments how many times "bob" appears
    i += 1 # increments i

# print out the result
print(count) 