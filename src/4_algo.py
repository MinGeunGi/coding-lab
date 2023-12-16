names = ['amy', 'Tom', 'Jerry', 'Tom', 'Mike', 'sun']
same_name = []
list_len = len(names)
for i in range(list_len):
    for j in range(i+1, list_len):

        if names[i] == names[j]:
            same_name.append(names[i])
            break
print(same_name)
            

