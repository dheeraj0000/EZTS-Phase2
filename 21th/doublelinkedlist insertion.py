class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=' ')
                temp=temp.next
    def insert_start(self,data):
        n=Node(data)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insert_last(self,data):
        n=Node(data)
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next

        np.next=temp.next
        temp.next=np
    
    '''
    def delete_last(self,data):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next                
        prev.next = None
    '''
        
        
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_start(1000)
l.insert_last(200)
#l.delete_last(200)
l.insert_position(3,400)
l.display()