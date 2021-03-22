def funct(arr, a=0, dict={}):
    if a < len(arr):
        if arr[a][0] not in dict.keys():
            dict[arr[a][0]] = len(arr[a])
        else:
            if dict.get(arr[a][0]) < len(arr[a]):
                dict[arr[a][0]] = len(arr[a])
        funct(arr, a+1, dict)
    return [[k,v] for k,v in dict.items()]

arr = ['aa', 'aaaaaaa', 'b', 'b', 'bbbbb']
print(funct(arr))