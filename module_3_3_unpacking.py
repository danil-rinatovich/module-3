def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [1.3, 'char']
values_dict = {'a': 2, 'b': 'str', 'c': False}
values_list_2 = [values_list, True]

print_params(123)
print_params(321, 'False')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print()
print_params(values_list)
print_params(values_dict)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_dict)
print()
print_params(values_list_2)
print_params(*values_list_2)
print_params(*values_list_2, 42)
