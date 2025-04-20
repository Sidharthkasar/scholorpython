sql={1,2,4,5}
python={1,6,7,8}
aws={1,4,5,6,99}
# subscribe 3 channel
print(sql.intersection(python).intersection(aws))
# only single channel
print(sql.symmetric_difference(python).symmetric_difference(aws))
# how many people are there
print(sql.union(python).union(aws))
# only python channel
print(python.difference(sql).difference(aws))
# only two channels
print(sql.symmetric_difference(python))
# only sql and aws
print(sql.intersection(aws))
