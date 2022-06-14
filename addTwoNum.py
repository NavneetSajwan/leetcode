class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_number(ll):
    temp  = ll
    count = 0
    num=0
    while(temp):
        num = num + temp.val*(10**count)
        count +=1
        temp = temp.next
    return num

def list_to_ll(total_list):
    prev_node = None
    for i in range(len(total_list), 0, -1):
        item = total_list[i-1]
        node = ListNode(val = item, next= prev_node)
        prev_node = node
    return node




def addTwoNumbers(l1, l2):
    num1 = get_number(l1)
    num2 = get_number(l2)
    total_list = str(num1+num2)
    print(total_list)
    return list_to_ll(total_list)

addTwoNumbers(list_to_ll([2,4,9]), list_to_ll([5,6,4,9]))
