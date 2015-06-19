class Node:

    def __init__(self,data):

          self.data = data
          self.left = None
          self.right = None
          self.parent = None

    def __str__(self):

          return str(self.data)

    def isLeft(self):

          return self.parent and self.parent.left == self

    def isRight(self):

            return self.parent and self.parent.right == self

    def hasAnychildren(self):
            return self.right or self.left

    def hasLeft(self):
            return self.left

    def hasRight(self):
            return self.right

    def hasBothchildren(self):
            return self.right and self.left



class BSTree:

    def __init__(self):

          self.root = None
          self.size = 0

    def __iter__(self):
        return self.root.__iter__()


    def create(self, val):

        if not self.root:

             self.root = Node(val)

        else:

             current = self.root

             while True:

                if val < current.data:

                   if current.hasLeft():
                      current = current.left
                   else:
                      current.left = Node(val)

                      break

                elif val > current.data:

                    if current.hasRight():
                       current = current.right
                    else:
                       current.right = Node(val)
                       break

                else:
                    break
        self.size += 1




    def bft(self): #Breadth-First Traversal

          self.root.level = 0
          queue = [self.root]
          out = []
          current_level = self.root.level

          while len(queue) > 0:

                current_node = queue.pop(0)

                if current_node.level > current_level:
                    current_level += 1
                    out.append("\n")

                out.append(str(current_node.data) + " ")

                if current_node.left:

                    current_node.left.level = current_level + 1
                    queue.append(current_node.left)

                if current_node.right:

                    current_node.right.level = current_level + 1
                    queue.append(current_node.right)

          print "".join(out)




    def Find(self,node,val):

            if(node.data == val):
                    return node


            elif(node.data < val):

                    return self.Find(node.right,val)

            else:

                    return self.Find(node.left,val)



    def successor(self,val):

        current = self.Find(self.root,val)
        if not current:
            return None
        if current.right:
            return self.findMin(current.right)
        else :
            succ = Node(None)
            ancestor = self.root

            while (ancestor != current):
                if(current.data)< (ancestor.data):
                    succ = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return succ




    def inorder(self,node):

           if node is not None:

              self.inorder(node.left)
              print node.data
              self.inorder(node.right)


    def lca(self,node,val1,val2):


            print node1.data , node2.data


            if (node.data > val1 and node.data > val2):
                return self.lca(node.left,val1,val2)
            elif (node.data < val1 and node.data < val2):
                return self.lca(node.right,val1,val2)

            return node

    def preorder(self,node):

           if node is not None:

              print node.data
              self.preorder(node.left)
              self.preorder(node.right)

    def findMin(self,node):

            current = node
            while current.hasLeft():
                current = current.left
            return current.data

    def postorder(self,node):

           if node is not None:

              self.postorder(node.left)
              self.postorder(node.right)
              print node.data








tree = BSTree()
arr = [20,8,22,4,12,10,14]
for i in arr:
    tree.create(i)

print tree.lca(tree.root,10,12)
