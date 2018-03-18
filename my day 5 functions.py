items = ["Mic", "Phone", 323.12, 3123.12, "Justin", "Bag", "Cliff Bars", 134]

str_items = []
num_items = []

for i in items:
	if isinstance(i, float) or isinstance(i, int):
		num_items.append(i)
	elif isinstance(i, str)
		str_items.append(i)
	else
	pass

print(str_items)
print(num_items)

def parse_lists(some_list):
    str_list_items = []
    num_list_items= []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            num_list_items.append(i)
        elif isinstance(i, str):
            str_list_items.append(i)
        else:
            pass
    return str_list_items, num_list_items

print(parse_lists(items))

items2 = ["Mic", "Phone", [123, 3234, "afeds"]]

print(parse_lists(items2))  #this only returns the "Mic" and "Phone"
# along with "[]" because it's a list object.


items3 = ["Mic", "Phone", 323.12, 3123.12, "Justin", "Bag", "Cliff Bars", 134]

sum(45, 342, 18)
sum([45, 342, 18])

def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

def count_num(my_num_list):
    count = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            count += 1
    return count

count_num(items3)

sum(items3) #this won't work, has alphas in list

my_sum(items3) #my function does work


def my_avg(my_num_list):
    the_sum = my_sum(my_num_list)
    number_of_items = count_num(my_num_list)
    return the_sum / (number_of_items * 1.0)

my_avg(items3)

#bonus- combine the sum and avg functions into one

list1a = [45, 22, 154, 17, "fred", "adam", 14, 202, 198]

def my_sum_avg(list_sum_avg):
    total = 0
    count = 0
    avg = 0
    for i in list_sum_avg:
        if isinstance(i, float) or isinstance(i, int):
            total += i
            count += 1
        else:
            pass
    avg = (total*1.0)/count
     
    return avg, total
    

my_sum_avg(list1a)





