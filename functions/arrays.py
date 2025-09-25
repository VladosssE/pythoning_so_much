def array_create(width):
    Array = []
    count = 1
    for i in range(width):
        elements = input(f"[ {count} ] Введите элементы массива: ")
        Array.append(elements)
        count += 1
    return Array


def array_find(Array, target):
    found = []
    count_found = 0
    
    for i, value in enumerate(Array):
        if value == target:
            found.append(i)
            count_found += 1
    if count_found == 0:
        return f"Значение {target} не найдено ни в какой позиции"
    return f"Значение {target} найдено в позициях {found}"


def array_add(Array, add, pos):
    Array.insert(pos, add)
    return Array


def array_change(Array, change, pos, width):
    if pos > width or pos < 0:
        return "\033[31m\n[ Ошибка: Позиция не найдена ]\033[0m"
    else:
        Array[pos] = change
        return Array


def array_delete(Array, delete, width):
    delete = str(delete)
    how_many_in_array = Array.count(delete)
    how_many_to_remove = min(how_many_in_array, width)
    
    if how_many_in_array == 0:
        return "Элемент не найден"
    else:
        for i in range(how_many_to_remove):
            Array.remove(delete)
    return Array
