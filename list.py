list_1 = [10,21,33,40,50,50]

#for i in range (len(list_1)):
#   print(i,list_1[i])
#print(list_1[0:4])
sum = 0
#for i in list_1:
#    sum = sum + i
#print(sum)
#print(i)  
#print("before append",list_1)
#list_1.append(60)
#print("after append",list_1)
#list_1.clear()
#print("after clear",list_1)
list_2 = list_1.copy()
print("after copy",list_2)
cnt =list_1.count(50)
count = 0
# for i in list_1:
#     if(i==50):
#         count = count+1
#     else:
#         count = count
# print(count)
 
even_list =[]
odd_list = []          
# for i in list_1:
#     if(i%2==0):
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(even_list)
# print(odd_list)   

list_1.insert(0,100)
print("after insert",list_1)