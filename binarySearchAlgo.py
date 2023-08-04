def binary_search(arr, element):
    start = 0
    end = len(arr) - 1
    steps = 0

    while start <= end:
        print("Step", steps, ":", str(arr[start:end + 1]))

        steps += 1
        middle = (start + end) // 2

        if element == arr[middle]:
            return middle
        if element < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1, 3, 5, 7, 9, 11,13,14,15,126,155,1566,146765]
target = 15

result = binary_search(my_list, target)

if result != -1:
    print(f"Target element {target} found at index {result}.")
else:
    print(f"Target element {target} not found in the list.")