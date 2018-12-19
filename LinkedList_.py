class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		super(Node, self).__init__()
		self.data = data
		self.next = None

class SLL(object):
	"""docstring for SLL"""
	def __init__(self):
		super(SLL, self).__init__()
		self.head = None
	def print_sll(self):
		temp = self.head
		while temp is not None:
			print('data:', temp.data)
			temp=temp.next
	def insertBegin(self, value):
		temp = Node(value)
		temp.next = self.head
		self.head = temp
	def insertEnd(self, value):
		temp = self.head
		new_node = Node(value)
		if temp is None:
			self.head = new_node
			return
		while temp.next is not None:
			temp = temp.next
		temp.next = new_node


list1 = SLL()
list1.insertBegin(7)
print('--------')
list1.print_sll()
# list1.head = Node(3)

list1.head.next = Node(4)
print('--------')
list1.print_sll()

list1.insertBegin(233)
print('--------')
list1.print_sll()

list1=SLL()
list1.insertEnd(777)
list1.insertEnd(22)
list1.insertBegin(333)
print('--------')
list1.print_sll()
		
