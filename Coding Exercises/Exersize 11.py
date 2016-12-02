class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x

    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print "List: ",",".join(values)

    def delete(self,x):
        if self.head == x:
            self.head = x.next
            x.next.prev = None
        elif self.tail == x:
            self.head= = x.prev
            x.prev.next = None
        else:    
            x.next.prev = x.prev
            x.prev.next = x.next
            x.next = None
            x.prev = None

if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.display()
