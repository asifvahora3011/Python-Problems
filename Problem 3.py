'''You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swapping the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]'''
# lst=[int(item) for item in input().split()]
# print(lst)
# list=()
# list= input("Enter a list:").split()
# for item in list:
#     print(item)
# list=[item for item in input("Enter a list:").split(",")] #comprehensive form
# list.reverse()
# print(list)
#
# list=[]
# user=input("Enter a list:").split(",")
# for item in user:
#     list.append(item)
# print(list)


n = int(input("enter list length:"))
lst=[]
for item in range(n):
    element=(input("enter an element of a list:"))
    lst.append(element)
print(f"Your list is:{lst}")
reverse1=lst[:] #To make a copy of lst
reverse1.reverse()
print(f"The first reverse of {lst} is {reverse1}")
reverse2 = lst[::-1]
print(f"The second reverse of {lst} is {lst[::-1]}")
reverse3 = lst[:]
for i in range(len(reverse3)//2): #List will be reversed in half length
    reverse3[i],reverse3[len(reverse3)-i-1] = reverse3[len(reverse3)-i-1], reverse3[i] #i=0, 4-0-1=3 
    # print(f"The reversed list at i={i} is {reverse3}")
print(f"The third reverse of {lst} is {reverse3}")
if reverse1==reverse2 and reverse2==reverse3:
    print("All lists are same")
else:
    print("All lists are not same")
