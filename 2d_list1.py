list_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
       
# print(list_2)

# for i in range (5):
#     for j in range (5):
#         print(i,j)

num_of_rows = len(list_2)

# for row in range(num_of_rows):
#     col_size = len(list_2[row])
#     for col in range(col_size):
#         print(list_2[row][col])
for row in list_2: #row = 0;1;
    print(row)
    for col in row:
        print(col) #0,0 #0,1 #0,2; #0,0 #0,1
 
list_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
 
even_list =[]
odd_list = []          
for i in list_2:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list) 

list_2 = [10,26,12,18]
even_list =[]
odd_list = []          
for i in list_2:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list) 
