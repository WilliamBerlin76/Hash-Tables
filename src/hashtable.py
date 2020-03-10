# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index] is not None:
            # print(f'WARNING: index: {index} already exists in storage')
            new_item = LinkedPair(key, value)
            new_item.next = self.storage[index]
            self.storage[index] = new_item  
        else:
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index]:
            self.storage[index] = None
        # elif self.storage[index].next is not None:
        #     self.storage[index] = self.storage[index].next
        else:
            return f'WARNING: index: {index} does not exist in storage'
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        # if self.storage[index] is not None:
        #     if self.storage[index].next is not None:
        #         if self.storage[index].next.key == key:
        #             return self.storage[index].next.key, self.storage[index].next.value
        #         else:
        #             return self.storage[index].key, self.storage[index].value
        #     else:
        #         return self.storage[index].key, self.storage[index].value

        # ATTEMPT WITH WHILE LOOP BELOW        
        if self.storage[index] is not None:
            
            if self.storage[index].key != key:
                cur = self.storage[index].next
                while cur is not None:
                    if cur.key == key:
                        return cur.value
                    else:
                        cur = cur.next
            elif self.storage[index].key == key:
                return self.storage[index].value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        i = 0
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(0, len(self.storage)):
            if self.storage[i] is not None:
                cur = self.storage[i]
                if cur.next is not None:
                    while cur is not None:
                        index = self._hash_mod(cur.key)
                        if new_storage[index] is not None:
                            new_item = LinkedPair(cur.key, cur.value)
                            new_item.next = new_storage[index]
                            new_storage[index] = new_item
                            cur = cur.next
                        else: 
                            new_storage[index] = cur
                            cur = cur.next
                else:
                    index = self._hash_mod(cur.key)
                    if new_storage[index] is not None:
                        new_item = LinkedPair(cur.key, cur.value)
                        new_item.next = new_storage[index]
                        new_storage[index] = new_item
                    else:
                        new_storage[index] = cur
           
        self.storage = new_storage
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
