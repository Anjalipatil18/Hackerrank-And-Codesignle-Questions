num = int(input("Enter a number: "))  

if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  



start = 11
end = 25
  
for val in range(start, end + 1): 
      
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val) 
