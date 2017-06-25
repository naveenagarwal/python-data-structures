class Node(object):
  """docstring for Node"""
  def __init__(self, data, next_node=None, prev_node=None):
    self.data = data
    self.next = next_node
    self.prev = prev_node

class UnorderedDoublyLinkedList(object):
  """docstring for ClassName"""
  def __init__(self):
    self.size = 0
    self.base = None

  def base_prev(self):
    print(self.base.prev)

  def add(self, data):
    node = Node(data, self.base)

    if self.base:
      self.base.prev = node

    self.base = node
    self.size += 1

  def remove(self, data):
    node = self.base

    while node:
      if node.data == data:
        prev_node = node.prev
        next_node = node.next
        if prev_node:
          prev_node.next = next_node
        if next_node:
          next_node.prev = prev_node

      node = node.next

  def list(self):
    node = self.base
    last_node = None
    print("in sequence ")
    while node:
      print(node.data)
      node = node.next
      if node != None:
        last_node = node

    print('in reverse order')
    node = last_node
    while node:
      print(node.data)
      node = node.prev

linked_list = UnorderedDoublyLinkedList()
linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
linked_list.base_prev()
linked_list.list()
linked_list.remove(10)
linked_list.list()
