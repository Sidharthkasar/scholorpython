print("Hello😉".upper())


#ord
# print('A','ord--->',ord('A'))
# print('a','ord--->',ord('a'))

# print(65,'chr -->',chr(65))
# print(97,'chr -->',chr(97))

# #ord upper to lower case
# val='ABC'
# for x in val:
#     ord_val=ord(x)
#     conv_chr=ord_val+32
#     print(chr(conv_chr))

# #ord lower to upper
# val='abc'
# for x in val:
#     ord_val=ord(x)
#     conv_chr=ord_val-32
#     print(chr(conv_chr))


#Swapcase manually
val='ABcTuuO'
for x in val:
    ord_val=ord(x)
    if ord_val in range(65,91):
        print(chr(ord_val+32),end='')
    elif ord_val in range(97,123):
        print(chr(ord_val-32),end='')
    else:
        print(x,end='')