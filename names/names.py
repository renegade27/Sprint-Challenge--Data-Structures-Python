import time

from dll_stack import Stack

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
notDupe = {}
stack = Stack()
for name_1 in names_1:
    stack.push(name_1)
for name_2 in names_2:
    stack.push(name_2)
while stack.storage.length != 0:
    popped = stack.pop()
    try:
        notDupe[popped]
        duplicates.append(popped)
    except:
        notDupe[popped] = stack.storage.length

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

