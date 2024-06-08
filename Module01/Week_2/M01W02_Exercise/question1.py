def max_kernel(num_list, k):
    return [max(num_list[0:i+k]) for i in range(len(num_list)-k+1)]
assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44 , 5 , 10, 12 , 33, 1]
k = 3
print(max_kernel(num_list, k))