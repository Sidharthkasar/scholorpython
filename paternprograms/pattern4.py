for row in range(5):
    for col in range(row+1):
        print('*',end=' ')
    print()
for row in range(4):
    for col in range(4-row):
        print('*',end=' ')
    print()

# Output:
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *