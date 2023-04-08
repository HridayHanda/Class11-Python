# def mul(x,y):
#     return x*y




# a = int(input("enter a "))
# b = int(input("enter b "))
# c = mul(a,b)
# print(c)





# def add(x,y):
#     return x+y
# def multiply(x,y):
#     return x*y
# def sub(x,y):
#     return x-y
# def divide(x,y):
#     return x/y

# # addition sub multiply division
# while True:
#     option = input("enter your option(A,M,S,D) : ")
#     if option not in "ASMD":
#         print('Wrong Input')
#     else:
#         a = int(input("enter a "))
#         b = int(input("enter b "))
#         if option in 'Aa':
#             c = add(a,b)
#             print(c)   

#         elif option in "Mn":
#             c = multiply(a,b)
#             print(c)   

#         elif option in "Ss":
#             c = sub(a,b)
#             print(c)   

#         elif option in "Dd":
#             c = divide(a,b)
#             print(c)   




#  prime no
# def prime(n):
#     for i in range(2,n):
#         if n % i ==0:
#             return "not prime"
#     else:
#         return ("prime")
# n = int(input("enter a number : ")) 
        
# k = prime(n)
# print(k)





# finding sum of odd number between two number
# def number(x,y):
#     sum = 0 
#     for i in range(x,y+1):
#         if i % 2 != 0:
#             sum += i  
#     return sum         
    
# a = int(input("enter a : "))
# b = int(input("enter b : "))
# print("sum of odd numbers", number(a,b))









# finding sum of even number between two number 
# def number(x,y):
#     sum = 0 
#     for i in range(x,y+1):
#         if i % 2 == 0:
#             sum += i  
#     return sum         
    
# a = int(input("enter a : "))
# b = int(input("enter b : "))
# print("sum of odd numbers", number(a,b))






# def prime(x,y):
#     l1 = []
#     for i in range(x,y+1):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else :
#             l1.append(i)
#     return l1








# a = int(input("enter a : "))
# b = int(input("enter b : "))
# print("list of prime ", prime(a,b))











# def prime(n):
#     l1 = []
#     i = 2 
#     while len(l1) < n :
#         for j in range(2,i):
#             if i%j == 0:
#                 i +=1
                     
#                 break
#         else :
#             l1.append(i)
#             i+=1
#         return l1








# a = int(input("enter a : "))
# print("list of prime ", prime(a))







def string(x):
    v = ""
    for  i in x:
        if i in "aeiouAEIOU":
            v +="*"
        else:
            v +=i
    return v
print(string('i am good'))




















# def wordreplace(x,y,z):
    
#     l2 = []
#     l1 = x.split(" ")
#     for i in l1:
#         if i == y:
#             l2.append(z)
#         else:
#             l2.append(i)
#     s = " ".join(l2)
#     return s
# print(wordreplace("hi how are you i am good how are you","how","what"))










        
        
    

    
    
 
   

    








