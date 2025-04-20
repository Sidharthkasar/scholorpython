#  triangle pattern of stars
for row in range(5):
    for col in range(5-row):
        print(' ',end='')
    for col in range(row):
        print('*',end=' ')
    print()