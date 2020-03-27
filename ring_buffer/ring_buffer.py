from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.head == None:
            self.storage.add_to_head(item)
        
        if self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = item
            # curr_head = item
            new_item = item

            self.storage.remove_from_tail()
            self.storage.add_to_tail(new_item)
        
        if self.storage.length > self.capacity:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            
        

        



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
         
        list_buffer_contents.append(self.current)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
