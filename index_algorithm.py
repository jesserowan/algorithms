some_list = [1, 2, 3, 4, 5, 7, 9, 10, 11, 15, 21, 34, 35, 36, 37, 88, 89]
def index(list):
    some_string = ""
    for x in range(len(list)-1):
        if list[x]+1 != list[x+1]:
            some_string += str(list[x]) + ", "
        elif list[x]+1 == list[x+1] and list[x]-1 != list[x-1]:
            some_string += str(list[x]) + "-"
    some_string += str(list[len(list)-1])
    return some_string

print(index(some_list))