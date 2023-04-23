# функция убирает дупликаты из отсортированного списка in place

def remove_duplicates(lst):
    pointer_1 = 0
    pointer_2 = 0

    while pointer_2 < len(lst):
        while pointer_2 < len(lst) - 1 and lst[pointer_2] == lst[pointer_2 + 1]:
            pointer_2 += 1
        
        lst[pointer_1] = lst[pointer_2]
        pointer_1 += 1
        pointer_2 += 1
    
    return lst[:pointer_1]
