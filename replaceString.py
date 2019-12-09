def replacestring(string):
    vowel="aeiou"
    i=0
    new_list=[]
    while i<len(string):
        if string[i] n vowel:
            s=string[i].upper()
            new_list=new_list+s
        else:
            new_list=new_list+string[i]
        i=i+1
    return new_list
print replacestring("navgurukul")