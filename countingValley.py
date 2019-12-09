def countingValleys(n, s):
    level = 0
    count = 0
    for i in s:
        if i=="U":
            level+=1
        if i=="D":
            level-=1
        if (level==0 and i=="U"):
            count+=1
    return count 
countingValleys(8,'UDDDUDUU')