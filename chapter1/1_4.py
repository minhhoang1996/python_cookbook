import heapq


# Finding the largest or smallest N items
nums = [3, 5, 1, 7, 23, 4, 3]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
print(cheap)

cheap = heapq.nlargest(1, portfolio, key=lambda s: s['price'])
print(cheap)

# If you are looking for the N smallest or largest items and N is small compared to the
# overall size of the collection, these functions provide superior performance.
nums = [1, 4, -33, 55, 3, 99, 45, 5, 2]
head = list(nums)
heapq.heapify(head)
print(heapq.heappop(head))
print(heapq.heappop(head))

# => The nlargest() and nsmallest() functions are most appropriate if you are trying to
# find a relatively small number of items.
# => If you are simply trying to find the single smallest
# or largest item (N=1), it is faster to use min() and max(). Similarly, if N is about the
# same size as the collection itself, it is usually faster to sort it first and take a slice (i.e.,
# use sorted(items)[:N] or sorted(items)[-N:]).
