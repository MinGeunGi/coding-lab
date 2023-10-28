
def print_max(my_list: list):
    list_len = len(my_list)
    if list_len == 0:
        return

    max_value = my_list[0]
    for i in range(list_len):
        if max_value < my_list[i]:
            max_value = my_list[i]

    return max_value


# value = [12, 34, 6, 3, 8, 100]
value = []
result = print_max(value)
print(result)
