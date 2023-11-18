

name_list = ['ff', 'aa', 'bb', 'aa', 'cc', 'dd', 'ee']
for i in range(len(name_list)):
    for name in name_list[i+1:]:
        if name_list[i] == name:
            print(name_list[i])

