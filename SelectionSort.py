def selection_sort(data, n):
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        temp = data[i]
        data[i] = data[min_index]
        data[min_index] = temp
    return data

data = input("Enter the list of numbers separated by spaces: ").split()
data = [int(num) for num in data]
n = len(data)
result = selection_sort(data, n)
print("The sorted list is:", result)