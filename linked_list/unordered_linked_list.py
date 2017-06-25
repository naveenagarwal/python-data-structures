class Node(object):
  """docstring for Node"""
  def __init__(self, data, next_node=None):
    self.data = data
    self.next = next_node


class UnorderedLinkedList(object):
  """docstring for LinkedList"""
  def __init__(self):
    self.size = 0
    self.base = None


  def add(self, data):
    node = Node(data, self.base)
    self.base = node
    self.size += 1

  def remove(self, data):
    node = self.base
    prev = None
    while node:
      if node.data == data:
        if prev:
          prev.next = node.next
        else:
          self.base = node

        self.size -= 1
        return True
      else:
        prev = node
        node = node.next

    return False

  def list(self):
    print('size is {}'.format( self.size))
    node = self.base
    while node:
      print(node.data)
      node = node.next

  def find(self, data):
    node = self.base
    while node:
      if node.data == data:
        return True
      else:
        node = node.next
    return False



linked_list = UnorderedLinkedList()

linked_list.add(20)
linked_list.add(10)
linked_list.add(40)
linked_list.add(50)

linked_list.list()

linked_list.remove(40)

linked_list.list()

print(linked_list.find(10))
print(linked_list.find(40))