# list compression
print([x for x in [1,3,4,5,6,7] if x%2==1])

# 2
print([f'even value{x}'if x%2==0 else f'odd value{x}' for x in [1,3,4,5,6,7]])

# 3
print([x for x in range(1,11) if x%2==0])