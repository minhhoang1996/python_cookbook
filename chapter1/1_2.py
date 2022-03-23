# Unpacking Elements from Iterables of Arbitrary Length
record = ("example", "abc@example.com", 13, 22, 39, 10)
name, mail, *numbers = record

print(name)    # return "hoang"
print(mail)    # return "abc@example.com"
print(numbers)    # return [13, 22, 39, 10]

# The starred variable can also be the first one in the list
numbers_record = [3, 5, 1, 6, 8, 33]
*trailing_nums, current_num = numbers_record
print(trailing_nums)
print(current_num)

# a sequence of tuples of varying length
records = [('Hoang', 12, 2),
           ('Hung', 4),
           ('Nam', 5, 1, 66)]
for name, *numbers in records:
    print(name, numbers)

##
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year), = record
print(name, year)



