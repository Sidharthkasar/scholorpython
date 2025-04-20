# reverse pattern of right angle triangle
for row in range(5,0,-1):
    for col in range(row):
        print('*',end=' ')
    print()

# Output:
# * * * * * 
# * * * * 
# * * *
# * *
# *