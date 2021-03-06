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

        according to http://www.cse.yorku.ca/~oz/hash.html
            the use of integer 33 has not been adequately explained
        '''
        hash_val = 5381
        for x in key:
            hash_val = hash_val * 33 + ord(x)
            # or
            # hash_val = ((hash_val << 5) + hash_val) + ord(x)
        return hash_val
        


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        if self.storage[index] is not None:
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
        if self.storage[index] is None:
            return f'WARNING: index: {index} does not exist in storage'
        elif self.storage[index].next is not None:
            self.storage[index] = self.storage[index].next
        else:
            self.storage[index] = None
        
            
            

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
         
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
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for i in range(len(old_storage)):
            cur = old_storage[i]
            if cur is not None:
                if cur.next is not None:
                    while cur is not None:
                        self.insert(cur.key, cur.value)
                        cur = cur.next
                else:
                    self.insert(cur.key, cur.value)
        
        

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
