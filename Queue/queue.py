# -*- coding: utf-8 -*-
"""queue.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1np7va7S1V1SWw1jdXuE0CWK8nZeWXalt
"""

class Queue:
  def __init__(self):
    self.arrays = []

  def dequeue(self):
    if not self.isEmpty():
      self.arrays.pop()
      return
    return "Empty Queue"

  def enqueue(self,contain):
    self.arrays.insert(0,contain)

  def peek(self):
    if not self.isEmpty():
      return self.arrays[len(self.arrays)-1]
    return "Empty Queue"

  def isEmpty(self):
    return self.arrays == []

  def display(self):
    print(self.arrays)

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()

q.dequeue()

q.display()

q.peek()

q.isEmpty()

q.dequeue()
q.dequeue()
q.dequeue()

q.peek()

q.isEmpty()

q.dequeue()