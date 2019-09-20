class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if None not in self.storage:
      if self.current >= self.capacity-1:
        self.current = 0
      self.storage[self.current] = item
      self.current += 1
      return
    self.storage[self.current] = item
    self.current += 1
    return
    

  def get(self):
    max = self.capacity
    for i in range(self.capacity):
      if self.storage[i-1] == None:
        max = i-1
    return self.storage[:max]