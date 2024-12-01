from Queue import *

def call_logs(calls, k):
    queue = Queue()
    for call in calls:
        queue.enqueue(call)
        if queue.size() > k:
            queue.dequeue()
    return queue.get_all()


print(call_logs([1, 2], k=3))
print(call_logs([1, 2, 3, 4, 5], k=2))
print(call_logs([], k=5))