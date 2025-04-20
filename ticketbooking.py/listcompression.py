# lst=[1,2,3,4,1,2]
# # op:[1,2,3,4]
# emp_list=[]
# for x in lst:
#     if x not in emp_list:
#         emp_list.append(x)
# print(emp_list)

# # list compression
# lst=[1,2,3,4,1,2]
# emp_list=[]
# [emp_list.append(x) for x in lst if x not in emp_list]
# print(emp_list)

# # print duplicate values
# lst=[1,2,3,4,1,2]
# # output: [1,2]
# emp_list=[]
# for x in lst:
#     if lst.count(x)>1:
#         emp_list.append(x)
# print(emp_list)

# print duplicates value
lst=[1,2,3,4,1,2]
emp_list=[]
dupl_list=[]
for x in lst:
    if x not in emp_list:
        emp_list.append(x)
    else:
        dupl_list.append(x)
print(dupl_list)