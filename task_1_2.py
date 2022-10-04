def check_min_1(lst_obj):
    """Функция должна возвращать минимальное значение из списка
    Алгоритм 1:
    Сложность: O(n**2).
    """
    min_el = lst_obj[0]
    for i in range(len(lst_obj)):              # O(n)
        for j in range(i + 1, len(lst_obj)):   # O(n)
            if min_el > lst_obj[j]:            # O(1)
                min_el = lst_obj[j]            # O(1)
    return min_el                              # O(1)


def check_min_2(lst_obj):
    """Функция должна возвращать минимальное значение из списка
    Алгоритм 2:
    Сложность: O(n).
    """
    min_el = lst_obj[0]
    for i in lst_obj:       # O(n)
        if i < min_el:      # O(1)
            min_el = i      # O(1)
    return min_el           # O(1)


list_1 = [10, 2, 15, 0, -5]

print(check_min_1(list_1))
print(check_min_2(list_1))
