# PROBLEM: https://leetcode.com/problems/min-stack/

# implement MinStack class
# which includes push(), pop(), top(), and getMin() functions
# ALL in constant time

class MinStack:
  def __init__(self):
    self.stack = []
    self.mins = []
  
  def push(self, val):
    self.stack.append(val)
    if len(self.mins) == 0:
      self.mins.append(val)
    else:
      if val < self.mins[-1]:
        self.mins.append(val)
      else:
        self.mins.append(self.mins[-1])
  
  def pop(self):
    self.stack.pop()
    self.mins.pop()

  def top(self):
    return self.stack[-1]
  
  def getMin(self):
    return self.mins[-1]


    
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2