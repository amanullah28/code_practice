import time
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time()-gen_start_time

list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_time = time.time()-list_start_time

print(f"tim taken by gen: {gen_time}")
print(f"tim taken by list: {list_time}")


