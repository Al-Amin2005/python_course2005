list_2 =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#print(list_2[2][1])
#print(len(list_2[1]))
# for i in range(5):
#     for j in range(5):
#         print(i,j)

num_of_rows = len(list_2)
for row in range(num_of_rows):
    col_size = len(list_2[row])
    for col in range(col_size):
        print(list_2[row][col])

