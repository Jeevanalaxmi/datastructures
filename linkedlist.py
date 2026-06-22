class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new
    def add_begin(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def display(self):
        itr=self.head
        while itr:
            print(itr.data,end='-->')
            itr=itr.next
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def remove_start(self):
        if self.head is None:
            return
        self.head=self.head.next
    def remove_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
    def add_position(self,data,pos):
        new=Node(data)
        if pos==0:
            new.next=self.head
            self.head=new
            return
        itr=self.head
        count=0
        while itr and count<pos-1:
            itr=itr.next
            count+=1
        if itr is None:
            print("Position out of bounds")
            return
        new.next=itr.next
        itr.next=new
    def create_loop(self,pos):
        if self.head is None:
            return
        loop_node=self.head
        count=0
        while loop_node and count<pos:
            loop_node=loop_node.next
            count+=1
        if loop_node is None:
            print("Position out of bounds")
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=loop_node
    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
    def find_duplicate(self):
        seen=set()
        duplicates=set()
        itr=self.head
        while itr:
            if itr.data in seen:
                duplicates.add(itr.data)
            else:
                seen.add(itr.data)
            itr=itr.next
        return duplicates
ll=LinkedList()
ll.add_begin(30)
ll.add_end(40)
ll.add_end(50)
ll.add_end(60)
ll.add_end(70)
ll.add_end(80)
ll.add_end(90)
ll.add_end(90)
ll.add_end(100)
ll.remove_start()
ll.remove_end()
ll.add_position(100, 5)
#ll.create_loop(2)
print("Middle element:", ll.middle())
print("Duplicates:", ll.find_duplicate())
ll.reverse()
ll.display()
#print("Elements:",ll.display())
#print("reversed elements:",ll.reverse())





