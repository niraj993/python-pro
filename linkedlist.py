class Node:
    def __init__(self,value):
        self.data = value
        self.address = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_node = 0

    def __len__(self):
        return self.num_of_node
    
    def insert_head(self,value):
        new_node = Node(value=value)
        new_node.address = self.head
        self.head = new_node

        self.num_of_node = self.num_of_node + 1

    

    def __str__(self):
        emplty_str = ''
        curr = self.head
        while curr != None:
            emplty_str = emplty_str + str(curr.data) + "->"
            curr = curr.address
        return emplty_str[:-2]
    

    def append(self,value):
        new_node = Node(value=value)
        if self.head == None:
            self.head = new_node
            self.num_of_node += 1
            return 
      
        curr = self.head
        while curr.address != None:
            curr = curr.address
        curr.address = new_node
        self.num_of_node += 1
        

    def insert_after(self,after,value):
        new_node = Node(value=value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.address

        if curr !=None:
            new_node.address = curr.address
            curr.address = new_node
            self.num_of_node += 1

        else:
            return "Item Not Found in Node"
        
    
    def clear(self):
        self.head=None
        self.num_of_node = 0


    def delete_head(self):
        if self.head == None:
            return "Empty LL"
        self.head = self.head.address
        self.num_of_node -= 1


    def delete_tail(self):
        if self.head ==None:
            return "Empty LL"
        
        curr = self.head

        if curr.address == None:
            return self.delete_head()
        
        while curr.address.address != None:
            curr = curr.address
        
        curr.address = None
        self.num_of_node -= 1


    def remove(self,value):
        if self.head == None:
            return "Empty LL"
        
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head

        while curr.address != None:
            if curr.address.data == value:
                break
            curr = curr.address

        
        if curr.address == None:
            return "Value Not Found"
        else:
            curr.address = curr.address.address



    def search(self,item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.address
            pos = pos + 1
        return "Not Found Item"
    

    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.address
            pos = pos + 1
        return "Index Out of the range"
    

    





obj_lin = LinkedList()
obj_lin.insert_head(1)
obj_lin.insert_head(2)
obj_lin.insert_head(3)
obj_lin.insert_head(4)
 

print(len(obj_lin))
print(obj_lin[0])
    
