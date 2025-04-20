# num=int(input('enter number'))
# if num<0:
#     print('-ve numeber')
# elif num>0:
#     print('+ve number')
# else: 
#     print('numb is zero')





maths=int(input('enter maths marks'))
phy=int(input('enter phy marks'))
chem=int(input('enter chem marks'))

total_marks=600
total_sum=maths+phy+chem
percent=(total_sum/total_marks)*100
print(percent)
if percent<35:
    print('Grade is f')
elif percent>35 and percent<=50:
    print('grade is c')
elif percent in range(51,91):
    print('grade is B')
elif percent in range(91,101):
    print('grade is a')
else:
    print('invalid per')