
import sys, time

# nums = sys.stdin.readline()

sum = 0
result = ''
total_time = 0
start = time.perf_counter()
for num in range(100000):
    sum = sum + num
    result += f'sum = {sum}\n'
    # sys.stdout.write(f'sum = {sum}\n')
    # sys.stdout.flush()
sys.stdout.write(result)
sys.stdout.flush()

total_time = time.perf_counter() - start

print(f'total time required {total_time}s')
