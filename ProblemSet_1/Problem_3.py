#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. 
#For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

s = "azcbobobegghakl"

aux = ""
longest = s[0]

for c in s:
    if aux == "" or aux[-1] <= c:
        aux += c
    else:
        if len(longest) < len(aux):
            longest = aux
            aux = c
        else:
            aux = c
            
if len(longest) < len(aux):
    longest = aux
            
print("Longest substring in alphabetical order is: " + longest)