str1 = "Rage Rage against the dying of the light"
i = 0
str2 = ""
while(i<len(str1)):
    if str1[i] == " ":
        i+=1
        continue
    str2 += str1[i]
    i+=1
print (str2)