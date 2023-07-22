def bubble_sort(data, n):
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    return data

data = input("Enter a list of numbers, separated by spaces: ")
data = [int(x) for x in data.split()]  
n = len(data)
result = bubble_sort(data, n)
print("The sorted list is:", result)