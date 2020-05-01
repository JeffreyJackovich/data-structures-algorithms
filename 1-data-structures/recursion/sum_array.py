import matplotlib.pyplot as plt
import time

'''
    O(n*k)
'''

def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])

# print(sum_array([5,9,11]))


# n_steps = 10
# step_size = 1000000
# array_sizes = list(range(step_size, n_steps*step_size, step_size))
# big_array = list(range(n_steps*step_size))
# times = []
#
# # Calculate the time it takes for the slice function to run with different sizes of k
# for array_size in array_sizes:
#     start_time = time.time()
#     big_array[:array_size]
#     times.append(time.time() - start_time)
#
# # Graph the results
# plt.scatter(x=array_sizes, y=times)
# plt.ylim(top=max(times), bottom=min(times))
# plt.xlabel('Array Size')
# plt.ylabel('Time (seconds)')
# plt.plot()

'''
sum_array_index

'''

def sum_array_index(array, index):
    if index == 0:
        return array[index]
    else:
        return array[index] + sum_array_index(array, index - 1)

array = [5,9,11]
index = len(array) - 1
print(sum_array_index(array, index))

n_steps = 10
step_size = 200
array_sizes = list(range(step_size, n_steps * step_size, step_size))
big_array = list(range(n_steps * step_size))
sum_array_times = []
sum_array_index_times = []

for array_size in array_sizes:
    subset_array = big_array[:array_size]

    start_time = time.time()
    sum_array(subset_array)
    sum_array_times.append(time.time() - start_time)

    start_time = time.time()
    sum_array_index(subset_array, 0)
    sum_array_index_times.append(time.time() - start_time)

plt.scatter(x=array_sizes, y=sum_array_times, label='sum_array')
plt.scatter(x=array_sizes, y=sum_array_index_times, label='sum_array_index')
plt.ylim(
    top=max(sum_array_times + sum_array_index_times),
    bottom=min(sum_array_times + sum_array_index_times))
plt.legend()
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()