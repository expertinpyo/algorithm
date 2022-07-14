# 1-2
import queue

q = queue.Queue()
num_list = [1, 2, 3]
for i in num_list:
    q.put(i)
while not q:
    print(q.get())