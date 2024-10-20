data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def recursion(list_):
    summa = 0
    if isinstance(list_, (list, tuple, set)):
        for i in list_:
            summa += recursion(i)
    elif isinstance(list_, dict):
        for value in list_.values():
            summa += recursion(value)
        for key in list_.keys():
            summa += recursion(len(key))
    elif isinstance(list_, int):
        summa += list_
    elif isinstance(list_, str):
        summa += recursion(len(list_))
    return summa

summa = recursion(data_structure)
print(summa)