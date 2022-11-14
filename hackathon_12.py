# i=10
# while i>=1:
#     print(i)
#     i=i-1

# name=[1,2,3,4,5,6,7]
# print(name[::-1])


# num=[1,2,3,4,5,6,7,8,9]
# i=0
# a=0
# while i<len(num):
#     a=a+num[i]
#     # print(a)
#     i=i+1
# print(a)


# def remove_dup(s):
#     i = 0
#     while i < len(s):
#         j = i + 1
#         while j < len(s):
#             if s[i] == s[j]:
#                 del s[j]
#             else:  
#                 j += 1
#         i += 1
# s = ['pen','book','cat','pen','book']
# remove_dup(s)
# print(s)


# s = ['pen','book','cat','pen','book']
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s):
#         if s[i] == s[j]:
#             del s[j]
#         else:  
#             j += 1
#     i += 1
# print(s)



# list1=[]
# list2=[6,8,5,9]
# list3=list1+list2
# i=0
# while i<len(list3):
#     a=i
#     j=i+1
#     while j<len(list3):
#         if list3[a]>list3[j]:
#             a=j
#         j=j+1
#     list3[i],list3[a]=list3[a],list3[i]

#     i+=1
# print(list3)



# ********************   Q 4.duplicate **************************
# list=[3,1,4,7,6,4,6,1,3] 
# A =[]
# for i in list :
#     if i not in A: 
#         A.append(i)
#         B=A
# print(B)


# array1=[3,1,4,7]
# array2=[6,8,5,9]
# array=array1+array2
# print(array)
# i=0
# while i<len(array):
#     a=i
#     j=i+1
#     while j<len(array):
#         if array[a]>array[j]:
#             a=j
#         j=j+1
#     array[i],array[a]=array[a],array[i]
#     i+=1
# print(array)



# def mean(list_of_num):
#     a=0
#     total=0
#     for num in list_of_num:
#         total=total+num
#     return total/len(list_of_num)
# print(mean([3,1,4,7,6,4,6,1,3] ))  

# def mode (list_of_num):
#     max_count=(0,0)
#     for num in list_of_num:
#         a=list_of_num.count(num)
#         if a >max_count[0]:
#             max_count=(a,num)
#     return max_count[1]
# print(mode([3,1,4,7,6,4,6,1,3]))  


# def meadian(list_of_num):
#     list_of_num.sort()
#     if len(list_of_num)%2!=0:
#         middle_index=int((len(list_of_num)-1)/2)
#     return list_of_num[middle_index]
# elif len(list_of_num)%2==0:
#     middle_index_1=int(len(list_of_num)/2)
#     middle_index2



# def mean(list_of_num):
#     a=0
#     total=0
#     for num in list_of_num:
#         total=total+num
#     return total/len(list_of_num)
# print(mean([3,1,4,7,6,4,6,1,3] ))  

A=int(input(" your 1 number "))
B=int(input(" your 2 number  "))
if A > B :
    print("YES")
else:
    print("NO")