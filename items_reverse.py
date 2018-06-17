items = [["a","A"],["b","B"]]
items2 = []
for item in items:
    item.reverse()

items.sort(reverse=True)
for inner_item in items:
    items2.append(item)
