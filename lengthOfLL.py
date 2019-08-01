### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than length()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # implement this method
  # return the length of the linked list, an integer value
  def length(self):
    # Beginning of Linked List
    currentNode = self.head
    # Confirms the head isn't empty and starts counter at 1. Otherwise, it returns 0.
    if (self.head):
      counter = 1
    else:
      return 0
    while currentNode.next != None:
        # While the Linked List has a value, incriments counter and progresses to the next node.
      counter+=1
      currentNode = currentNode.next
      # Returns counter.
    return counter

ll = LinkedList()
ll.extend([1, 2, 3, 4, 5])
print(ll.length())
