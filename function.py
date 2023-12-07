
# count=0
# for i in str1:
#     count =count+1
# print(count)
# def custom_len(a,b):
#     count1=0
#     count2=0
#     for i in a:
#         count1 = count1+1
#     for j in b:
#         count2 = count2+1    
#     return count1,count2
# str1 = "alamin"  
# str2 = "alamin111"
# a,b = custom_len(str1,str2)
# print(a,b)
def custom_len(a,b):
    count1=0
    count2=0
    for i in zip(a,b):
        count1=count1+1
        count2=count2+1
    return count1,count2
str1="alamin"
str2="alamin"
a,b=custom_len(str1,str2)
print(a,b)    