def encrypt(string):
    str=""
    for i in string:
        str=i+str
    vowels={
            'a' : '0',
            'e' : '1',
            'o' : '2',
            'u' : '3'
            }
    result=""
    for i in str:
        for j in vowels:
            if i == j:
                i=vowels[j]
        result+=i
    res="aca"
    new=result+res
    print new
encrypt("karaca")