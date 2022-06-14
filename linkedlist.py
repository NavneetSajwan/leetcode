class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def list_to_ll(self, total_list):
        prev_node = None
        for i in range(len(total_list)):
            item = total_list[i]
            node = Node(data = item, next= prev_node)
            prev_node = node
        self.head = node

ll = LinkedList()
# ll.head = Node(1)
# second = Node(10)
# third = Node(4)
# ll.head.next = second
# second.next = third
ll.list_to_ll([25,45,13])

ll.print_list()