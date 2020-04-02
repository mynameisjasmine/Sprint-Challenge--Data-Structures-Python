from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if there is no head node, create one
        if self.current == None:
            self.current = self.storage.head
        
            
            # if the list is full, delete the oldest item and add new item to head          
        if self.capacity == len(self.storage) and self.current == self.storage.head:
                self.storage.remove_from_tail()
                self.storage.add_to_head(item)
                self.current = self.current.next
        
        if len(self.storage) < self.capacity and self.current == self.storage.head:
            # self.current = self.storage.head
            self.storage.add_to_head(item)
            self.current = self.current.next
                
                

                
            # elif count.value > self.capacity or self.current > self.capacity:
            #      self.current = 0
            # elif self.capacity > self.storage.length:
            #     #  self.storage.remove_from_tail()
            #     self.storage.add_to_tail(item)
    
        
        
        
        # if self.storage.head == None:
        #     self.storage.add_to_head(item)
        
        # if self.storage.head:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_head(item)
        #     self.current = item
        #     # curr_head = item
        #     new_item = item

        #     self.storage.remove_from_tail()
        #     self.storage.add_to_tail(new_item)
        
        # if self.storage.length > self.capacity:
        #     self.storage.remove_from_tail()
        #     self.storage.add_to_tail(item)
            
        

        



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
