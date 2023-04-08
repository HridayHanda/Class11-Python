# # linear searchh 
# def linearsearch(num,l1):
#     for i in range(len(l1)):
#         if l1[i]==num:
#             return True
#     else:
#         return False


# l1 =[1,23,4,5,7,45,65,34,6]
# n = 6
# print(linearsearch(n,l1))

















def binarysearch(num,target):
    l = 0 
    h = len(num)-1

    while l <= h:
        mid = (l+h)//2
        if num[mid] ==target:
            return mid
        else:
            if target < num[mid]:
                h = mid-1
            else:
                l = mid+1
    return -1



l1 =[1,23,4,5,7,45,65,34,6]
l1.sort()
n = 6
print(binarysearch(l1,n))



















# bubble sort 
def bubblesort(l1):
    n = len(l1)
    for i in range(n):
        for j in range(0,n-i-1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]


l1 = [5,1,4,3,8]
bubblesort(l1)
print(l1)









