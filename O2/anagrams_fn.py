def update_dict(dict, ch):
    if ch in dict:
        dict[ch] += 1
    else:
        dict[ch] = 1

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
dict1 = {}
dict2 = {}
for ch in list(str1):
    update_dict(dict1,ch)
for ch in list(str2):
    update_dict(dict2,ch)
if (dict1 == dict2):
    print("The two strings are anagrams")
    print(dict1)
else:
    print("The two strings are not anagrams")