class Node:

        def __init__(self, data = None, next= None):

            self.data = data
            self.next = next
    
        def __str__(self):

            return str(self.data)

class LinkedList:

        def __init__(self):

            self.head = None  #the top of list
            self.tail = None #last element of the list

#adding elements to the tail of the node.

        def insert(self, data):

            node = Node(data,None)

            if not self.head:
                self.head = self.next = node

            else :
                self.tail.next = node

            self.tail = node



        def delete(self,val):

            current = self.head
            next_current = None

            while current:
                if current.data == val:
                    if not next_current:
                        next_current.next = current.next
                    else :
                        self.head = current.next

                next_current = current
                current = current.next

        def printlist(self):

            if self.head is None:
                return None
            else:
                current = self.head

                while current is not None:
                    print current.data," ",
                    current = current.next
                    if current is None:
                        print None

sl = LinkedList()
sl.insert(31)
sl.insert(2)
sl.insert(3)


sl.printlist()






