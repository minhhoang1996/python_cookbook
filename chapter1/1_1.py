# Unpacking a Sequence into Separate Variable
data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
# print(name)
# print(date)

# you may sometimes want to discard certain values
_, shares, price, _ = data
print(shares)
print(price)





