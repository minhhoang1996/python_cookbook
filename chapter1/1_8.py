

prices = {
    'AD': 33.4,
    'DD': 43.5,
    'WE': 12.5
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.values()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# another way
print(min(prices, key=lambda k: prices[k]))
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)


