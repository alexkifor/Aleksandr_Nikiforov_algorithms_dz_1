# 1 способ
companies = {'Adidas': 19000.56, 'Nike': 25000.48, 'Zara': 45023.31, 'Puma': 2153.66, 'Demix': 1250.11}
profits = []                           #O(1)
while len(profits) < 3:                #O(n)
    max_val = 0                        #O(1)
    key_max = ''                       #O(1)
    for k, v in companies.items():     #O(n)
        if max_val < v:                #O(1)
            max_val = v                #O(1)
            key_max = k                #O(1)
    profits.append(key_max)            #O(1)
    companies.pop(key_max)             #O(n)
for i in profits:                      #0(1)
    print(i)                           #O(1)
# Итоговая сложность O(1) + O(n) * (O(1) + O(1) + O(n) * (O(1) + O(1) + O(1)) + O(1) + O(n)) + O(1) * O(1) = O(n**2)

# 2 способ
companies = {'Adidas': 19000.56, 'Nike': 25000.48, 'Zara': 45023.31, 'Puma': 2153.66, 'Demix': 1250.11}
sorted_keys = sorted(companies, key=companies.get, reverse=True)[:3]    #O(n log n)
for i in sorted_keys:                                                   #O(1)
    print(i)                                                            #O(1)
# Итоговая сложность O(n log n) + O(1) + O(1)
# Второй способ эффективнее, т.к. его сложность меньше O(n log n) меньше O(n**2)