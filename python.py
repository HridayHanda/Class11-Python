

# Str = "mynameishriday"
# for i in Str:
#     if i in ["a","e","i",'o','u']:
#         print("*",end='')
#     else:
#         print(i,end='')






# num = "0112345675"
# print(num[0:3]+"-"+num[3:6]+'-'+num[6::])






# Str = input("enter a string : ")
# print(Str.count(" ")+1)




# Str = input("enter a string : ")
# L1 = Str.split(" ")
# print(len(L1))




# vowels = input("enter a string")
# count=0
# for i in vowels:
#     if i in ["a",'i','o','u','e']:
#         count+=1
# print(count)














# name = input("enter a string : ")
# L1 = name.split(' ')
# for i in L1:
#     print(i[::-1],end=' ')



# name = "hridayhanda"
# print(name[::-2])









# print("hriday".find("y"))




# name = "abC"
# for i in name:
#     if i.islower():
#         print(i.upper(),end='')
#     else:
#         print(i.lower(),end='')
















# S1 = 'abcdefghijklmnopqrstuvwxyz'
# curpos = 0
# curtime = 0
# name = "pizza"
# for i in name:
#     distrav = abs(S1.index(i)-curpos)
#     curtime+=distrav
#     curpos = S1.index(i)
# # print(curtime)    









# S1 = 'abcdefghijklmnopqrstuvwxyz '
# curpos = 0
# curtime = 0
# name = "p izza"
# for i in name:
#     distrav = abs(S1.index(i)-curpos)
#     curtime+=distrav
#     curpos = S1.index(i)
# print(curtime)




















# A = eval(input("enter "))
# print(type(A))








# num = "4125"
# li = []
# for i in num:
#     li.append(i)

# print(li)
# li.reverse()
# print(li)
# print("".join(li))








# li = []
# name = ["chinu","Hriday","mayank","geeta"]
# for i in name:
#     if ("h" in i or 'H' in i or "e" in i):
#         li.append(i)        
# print(li)












# ti = tuple([1,2,3,4,5,6,(2,3)])
# print(ti)
















# a = ("hriday",)
# b = ("handa",)
# c = a+b
# print(c)








# li = []
# for i in range(1,51):
#     li.append(i**2)
# tup = tuple(li)
# print(tup)











# a = 0
# b = 1
# li =[0,1]
# for i in range(7):
#     c = a+b

#     li.append(c)
#     a=b
#     b=c
# print(tuple(li))



# l1 = [0,1]
# n = int(input("Enter a number : "))
# for i in range(2,n):
#     l1.append(l1[-1]+l1[-2])
# print(l1)


print('hello','hello')











# dic = {
#     '101':{
#         'name':'hriday',
#         'eng':94,
#         'math':97,
#         'sci':91,
#     }
# }

# dic['101']['physics'] = 70

# print(dic)














# dic = {
#     'a':1, 'b':2, 'c':3,'x':4
# }


# print(dic.values())









# dic = {
#     'a':1, 'b':2, 'c':3,'x':4
# }
# key = "y"
# value = 7 
# dic[key] = value
# print(dic)







#q5
# dic = {
#     'a':1, 'b':2, 'c':3,'x':4
# }
# for i in dic:
#     print(i," : ",dic[i])










# q4
# dic = {
#     'a':1, 'b':2, 'c':3,'x':4
# }
# a = input("enter a key : ")
# if a in dic.keys():
#     print("keys exist")
# else:
#     print("doesnt exist ")









# q6
# dic = {}
# n = int(input("enter a number"))
# for i in range(1,n+1):
#     dic[i]=i*i
# print(dic)






# q7
# dic = {}
# for i in range(1,16):
#     dic[i]=i*i
# print(dic)










# dic1 = {"a":1}
# dic2 = {"b":2}
# dic1.update(dic2)
# print(dic1)















# q10
# sum = 0 
# dic = {
#     'a':1, 'b':2, 'c':3,'x':4
# }
# for i in dic:
#     sum+=dic[i]
# print(sum)    







# q10
# sum = ""
# dic = {
#     'a':1, 'b':2, 'c':3,'x':4
# }
# for i in dic:
#     sum+=i
# print(sum)    








# q3
# dic1 = {"a":1,"b":2}
# dic2 = {"c":3,"d":4}
# dic3 = {"e":5,"f":6}
# dic = {}
# dic.update(dic1)
# dic.update(dic2)
# dic.update(dic3)
# print(dic)











# li = []
# for i in range(1,51):
#     li.append(i*i)
# tup = tuple(li)
# print(tup)  












# li = []
# count = 1
# ind = 97
# while count<=26:
#     li.append(chr(ind)*count)
#     count+=1
#     ind+=1
# print(li)












# vals = (1,4,7,5,8,9,9,8)
# mean = sum(vals)/len(vals)
# print(mean)
# sum = 0
# for i in vals:
#     sum+=((i-mean)**2)
# S = (sum/len(vals)-1)**0.5
# print(S)






# vals = (1,4,7,5,8,9,9,8)
# mean = sum(vals)/len(vals)
# print(mean)








# seqA = {1,2,3}
# seqB = {1,2,3,4,5}
# print(seqA.issubset(seqB))

# print((seqB))



#  WAP to input an integer list with 6 elements and create another 
# list which contains the integers ignoring the duplicate elements 
# from the first list. Finally disply both the lists.


# l1 = [1,2,3,4,5,6,]
# l2 = [1,1,5,3,5,6,8,3,4,8,9,5,0,9]

# l3 =[]

# for i in l1:
#     if i in l2:
#         l3.append(i)
#         for j in range(l2.count(i)):
#             l2.remove(i)


# print(l2+l3)


# WAP to input 2 lists with 5 elements each and merge them into one. Then print the merged list
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [12,13,14,14,15]



# print(l1 + l2)













# WAP to input a list of 5 integer elements and print the buzz numbers from it. Buzz numbers which have 7 as the last digit or are divisible by 7.


# l1 = [45,657,342,456,867,234,456,342,465,234,67, 70,768234,345,456,657]

# for i in l1:
#     if i%7 == 0:
#         print(i)
#     elif str(i)[-1] == '7':
#         print(i)











# WAP to input a list and print the largest and the smallest element in the list. Also, print the sum of the elements of the list

# l1 = [1,2,3,4,5,6,7,8,9]

# print(max(l1), min(l1), sum(l1))










# length = int(input('enter a length'))
# g = 0 
# for i in range(length,0,-1):
#     print(' '*g,'*'*(2*i-1))
#     g = g+1






# g = 0
# for i in range(5,0,-1):
#     print('* '*i)
#     g+=1






# l1 = []
# num = int(input("enter a num :"))
# for i in range(1,num+1):
#     if num%i==0:
#         l1.append(i)
# print(l1)










# para = input("enter a para : ")
# count = 0
# a = para.count("a")
# i = para.count("i")
# e = para.count("e")
# o = para.count("o")
# u = para.count("u")
# d1 = {"a":a,"e":e,"i":i,"o":o,"u":u}
# print(d1)









# l1 = [8,9,10]
# l1[1]=17
# l1.append(4)
# l1.append(5)
# l1.append(6)
# l1.pop(0)
# l1.sort()
# l1.extend(l1)
# l1.insert(3,25)







# sum = 0
# for i in range(1,10000000,2):
    
#     print(i)







# l1 = [1,2,3,4,5,6,7,8,9,10,11,23,4,5,7,7,8,8,6,5,4,78,98]
# sumodd = 0
# sumeven = 0
# for i in l1:
#     if i%2==1:
#         sumodd+=i
#     else:
#         sumeven+=i
# print("sum of odd no",sumodd)        
# print("sum of even no",sumeven)









# l1 = [1,34,45,65,45,6,4,5,67,4,6,44,456,765,77,999,1000,10339393,3485345678]
# a=max(l1)
# l1.remove(a)
# print(max(l1))






# l1 = [1,34,45,65,45,6,4,5,67,4,6,44,456,765,77,999,1000,10339393,3485345678]
# a=min(l1)
# l1.remove(a)
# print(min(l1))












# l1 = [2,3,4,5,6,7,8,9]
# l2 = [34,54,64,6,5,44,67]
# for i in l1:
#     if i in l2:
#         print("overlapped")
#         break
# else:
#     print('seperate')













# l1 = [2,3,4,6,7,5,6,5,45]
# mul = 1
# for i in l1:
#     mul*=i
# print(mul)    











# Q1. WAP to input an integer list with 6 elements and create another list which contains the integers ignoring the duplicate elements from the first list. Finally disply both the lists.
   
# l1 = []
# l2 = []
# for i in range(6):
#     a= int(input("enter a number : "))
#     l1.append(a)
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l1)
# print(l2)            


#<~~~~~~~~~~~ ~~~~~~~~~~~~~> 



# l1 = []
# l2 = []
# for i in range(6):
#     a= int(input("enter a number : "))
#     l1.append(a)
# for i in l1:
#     if l1.count(i)==1:
#         l2.append(i)
# print(l1)
# print(l2)            








# Q2. WAP to input 2 lists with 5 elements each and merge them into one. Then print the merged list.
   

# l1 = []
# l2 = []
# for i in range(5):
#     a = int(input("enter a number : "))
#     l1.append(a)
# for i in range(5):
#     a = int(input("enter a number : "))
#     l2.append(a) 
# print(l1)
# print(l2)
# print(l1+l2)


#>~~~~~~~~~~ ~~~~~~~~~~~~~~~~

# l1 = []
# l2 = []
# for j in (l1,l2):
#     for i in range(5):
#         a = int(input("enter a number : "))
#         j.append(a) 
# print(l1)
# print(l2)
# print(l1+l2)


# Q3. WAP to input a list of 5 integer elements and print the buzz numbers from it. Buzz numbers which have 7 as the last digit or are divisible by 7.
# l1 = []
# for i in range(5):
#     a = eval(input("enter a number : "))
#     l1.append(a)
# for i in l1:
#     if i%7==0 or str(i)[-1]=="7":
#         print(i)


   



# sumeven = 0
# sumodd = 0
# for i in range(1,999999999999999999999999):
#     if i%2==0:
#         sumeven+=i
#     else:
#         sumodd+=i        
# print("sum of even",sumeven)
# print("sum of odd",sumodd)











# def prime(num):
#     for i in range(2,num//2 + 1):
#         if num%i==0:
#            return(0)
#         else:
#            pass
#     return(1)
# for x in range(2,1000001):
# 	if prime(x)==1:
# 		print(x)









# l1  = []
# s = "hriday"
# for i in s:
#     l1.append(i)
# print(l1)
# print(str(l1)[0:3])
# print(''.join(l1))







# tupp = ()
# n = int(input("enter n numbers : "))
# for i in range(n):
#     v = int(input("Enter Number : "))
#     tupp += (v,)
# print(tupp)









# dict1 = {
#     "Amit":[22,10000],
#     "Rahul":[29,30000],
# }

# # print('Name','Age','Salary',sep='\t')

# # for i in dict1:
# #     print(i, dict1[i][0], dict1[i][1], sep='\t')


# dict2 = {
#     'Amit':{
#         'age': 29,
#         'sal': 25000
#     },
#     'Manisha':{
#         'age':21,
#         'sal':10000
#     },
#     'Hriday':{
#         'age':12,
#         'sal':200
#     }
# }

# print('Name','Age','Salary',sep='\t')

# for i in dict2:
#     print(i, dict2[i]['age'], dict2[i]['sal'], sep='\t')










# l1 = []
# for i in range(5,101,3):
#     l1.append(i)
# print(l1)



# print([x for x in range(5,101,3)])








# tup = (5,2,1,3,4)
# sorted(tup)
# print(tup)
# print(sorted(tup))
# tup = sorted(tup)
# print(tup)













# dic1 = {
#     1:1,
#     2:2,
#     3:3
# }

# del dic1[1]
# print(dic1)

# print(dic1)













# mydict = {"a":27,"b":43,"c":25,"d":30}
# valA = " "
# for i in mydict:
#     if i > valA:
#         valA = i 
#         valB = mydict[i]
# print(valA)
# print(valB)
# print(30 in mydict)
# mylst = (mydict.items())
# mylst.sort()
# print(mylst[-1])

















# n = 2587
# factors = []
# for i in range(2, n+1):
#     while n % i == 0:
#         factors.append(i)
#         n = n // i
# print(factors)

















# def string(x):
#     v = ""
#     for  i in x:
#         if i in "aeiouAEIOU":
#             v +="#"
#         else:
#             v +=i
#     return v
# print(string('The word pollution was derived from the Latin word pollution, which means to make dirty.')















# a = int(input("no of calls : "))
# if a <= 100:
#     print("0")
# elif a > 100 and a <= 500:
#     print((a-100)*2.5)
# elif a > 500 and a <=1000:
#     print((a-100)*4.5)
# else:
#     print((a-100)*7.5)
















# a = "Loves One and All"
# print(a[-3:])

# print(a[12:])

# print(a[10:-12])


# print(a[10:-12:-1])








# d1 = {1:"a",2:"b",3:"c",4:"d"}
# print(d1.items())
# print(len(d1))
# print(d1.get(1,"not found"))
# del d1[2]
# print(d1)
















# for a in range(10,21,3):
#     print(a)
    


















# def factorialno(x):
#     f = 1
#     for i in range(1,x+1):
#         f *=i
#     return f 
# a = int(input("enter a number : "))
# print(factorialno(a))










# l1 = [0,1]
# a = 10
# for i in range(a-2):
#     l1.append(l1[-1]+l1[-2])
# print(l1)


# a = "Hi i am hriday"
# di ={}
# for i in a:
#     di[i]=di.get(i,0)+1
# print(di) 















# stri = ''
# a = "computer science "
# for i in a:
#     if i not in "aeiouAEIOU":
#         stri+=i
# print(stri)








# l2 = []

# l1 = [-2,1,-3,-15,16,-17,5,-3,-6]
# for i in l1[::-1]:
#     if i < 0:
#         l2.append(i)
#     else:
#         l2.insert(0,i)
# print(l2)







# l2 = []

# l1 = [-2,1,-3,-15,16,-17,5,-3,-6]
# for i in l1[::-1]:
#     if i > 0:
#         l2.append(i)
#     else:
#         l2.insert(0,i)
# print(l2)














# l2 = []
# l1 = []
# a = int(input("enter elements"))
# for i in range(a):
#     x = int(input("enter numbers"))
#     l1.append(x)

# z = int(input("enter the elements youu want to search"))
# print(l1.count(z))

# for i in range(l1.count(z)):
#     c = l1.index(z)
#     l2.append(c)
#     l1[c]="#"
# print(l2)
















# s = 0

# a = int(input("enter elements"))
# l1 = list(str(a))
# print(l1)


# for i in l1:
#     s += int(i)

# print(s)
















# stri = "1love 2 to 3 my 4 bed 5 dancing 6 and gaming"
# aplha = 0
# digit = 0
# for i in stri:
#     if i.isalpha():
#         aplha+=1
#     elif i.isdigit():
#         digit+=1
# print("total number of aplhabets",aplha)
# print("total number of digits",digit)















# a = int(input("enter no of sudents : "))
# dic1 = {}
# for i in range(a):
#     name = input("enter name of the students : " )
#     medals = int(input("enter no of medals : "))
#     dic1[name]=medals

# print(dic1)    









# tup = ()
# a = int(input("enter numbers of digit : "))
# for i in range(a):
#     x =  int(input("enter numbers : "))
#     tup += (x,)
# print(min(tup))
# print(max(tup))












# num = 10 
# sum = 0
# for i in range(1,num+2,2):
#     if i %3 ==0:
#      continue
#     sum = sum + i
#     print(sum)









# text1 = "Half YeArLy XI 2022"
# text2 = ""
# I = 0
# while I<len(text1):
#     if text1[I]>="0" and text1[I]<="9":
#         val = int(text1[I])
#         val = val + 1
#         text2 = text2 + str(val)
#     elif text1[I]>="A" and text1[I]<="Z":
#         text2 = text2 + (text1[I+1])
#     else:
#         text2 = text2 + "*"
#     I = I+1
# print(text2)













# for k in range(4):
#     for j in range(k):
#         print("*",end=" ")
#     print()








































































































































































