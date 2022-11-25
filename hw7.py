
def binary_search(target, lst):
    l = 0
    r = len(lst)
    while l + 1 < r:
        m = (l + r) // 2
        if lst[m] == target:
            l = m
            r = m
            break
        elif lst[m] > target:
            r = m
        else:
            l = m + 1
    if lst[l] == target:
        print(f'Элемент найден под индексом {l}')
    else:
        print(f'Элемент не найден')


binary_search(7, [1, 2, 3, 6, 8, 9, 10])

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

print(bubble_sort([5,54, 3, 5, 5, 7,3, 4]))
