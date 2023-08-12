def min_max(list):
    if not list:
        return 'Empty list!'
    min = list[0]
    max = list[0]
    for i in range(1, len(list)):
        if list[i]>max:
            max = list[i]

        if list[i]<min:
            min = list[i]    
    return f'max = {max}, min = {min}'
    



list = [1, 2]
print(min_max(list))