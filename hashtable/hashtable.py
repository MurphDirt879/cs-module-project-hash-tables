# change to wroking

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.capacity = capacity
        self.itemCount = 0
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return len(self.data)
    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.itemCount / self.capacity
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here
    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        slot = self.data[index]
        while slot is not None and slot.key != key:
            slot = slot.next
        if slot is not None:
            slot.value = value
        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.data[index]
            self.data[index] = new_entry
            self.itemCount += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        slot = self.data[index]
        prev = None
        while slot is not None and slot.key != key:
            prev = slot
            slot = prev.next
        if slot is None:
            return None
        else:
            if prev is None:
                self.data[index] = slot.next
            else:
                prev.next = slot.next
            self.itemCount -= 1
            return slot
    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        slot = self.data[index]
        while slot is not None:
            if(slot.key == key):
                return slot.value
            slot = slot.next
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        oldData = self.data
        self.capacity = new_capacity
        self.data = [None] * new_capacity
        prev_entry = None
        for slot in oldData:
            prev_entry = slot
            while prev_entry is not None:
                self.put(prev_entry.key, prev_entry.value)
                prev_entry = prev_entry.next
if __name__ == "__main__":
    ht = HashTable(8)
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print("")
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print("")


