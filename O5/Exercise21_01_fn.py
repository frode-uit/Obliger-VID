# With linear probing
# Define the default hash-table size
DEFAULT_INITIAL_CAPACITY = 4
  
# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.5 
     
# Define the maximum hash-table size to be 2 ** 30
MAXIMUM_CAPACITY = 2 ** 30 
  
class Map:
    def __init__(self, capacity = DEFAULT_INITIAL_CAPACITY, 
                 loadFactorThreshold = DEFAULT_MAX_LOAD_FACTOR):
        # Current hash-table capacity. Capacity is a power of 2
        self.capacity = capacity

        # Specify a load factor used in the hash table
        self.loadFactorThreshold = loadFactorThreshold
   
        # Create a list of empty buckets
        self.table = [[None,None]]*self.capacity
                
        self.size = 0 # Initialize map size

    # Add an entry (key, value) into the map 
    def put(self, key, value):
        if self.size >= self.capacity * self.loadFactorThreshold:          
            if self.capacity == MAXIMUM_CAPACITY:
                raise RuntimeError("Exceeding maximum capacity")
      
            self.rehash()
    
        index = self.getHash(hash(key))

        # Add an entry (key, value) to hashTable[index]
        
        while (index < self.capacity):
            elem = self.table[index]
            if elem[0] != None:
                index += 1
            else:    
                self.table[index]= [key, value]
                break
       
        self.size += 1 # Increase size
 
    # Remove the entry for the specified key 
    def remove(self, key):
        
        index = self.getHash(hash(key))
    
        # Remove the first entry that matches the key
        while (index < self.capacity):
            elem = self.table[index]
            if elem[0] == key:
                self.table[index]= [None,None]
                self.size -= 1 # Decrease size
                break
            elif elem[0] == None:
                break
            else:    
                index += index
                               
            

    # Return true if the specified key is in the map
    def containsKey(self, key):
        if self.get(key) != None:
            return True
        else:
            return False
  
    # Return true if this map contains the specified value 
    def containsValue(self, value):
        if not self.isEmpty():
            for entry in self.table:
                if entry[1] == value:
                    return True
    
        return False
  
    # Return a set of entries in the map 
    def items(self):
        entries = []
    
        for entry in self.table:
            if entry[0] != None:
                entries.append(entry)
        return tuple(entries)
    
    # Return the first value that matches the specified key 
    def get(self, key):
        index = self.getHash(hash(key))
        if not self.isEmpty():
            while (True):
                entry = self.table[index]
                if entry[0] == key:
                    return entry[1]
                elif entry[0] == None:
                    break
                else:
                    index += 1
                    if index > self.capacity:
                        break
        return None
  
    # Return all values for the specified key in this map
    def getAll(self, key):
        values = []
        index = self.getHash(hash(key))
        if not self.isEmpty():
            while (True and index < self.capacity):
                entry = self.table[index]
                if entry[0] == None:
                    break
                elif entry[0] == key:
                    values.append(entry[1])
                index += 1
                
        return tuple(values)
  
    # Return a set consisting of the keys in this map
    def keys(self):
        keys = []
    
        for i in range(0, self.capacity):
            entry= self.table[i] 
            if entry[0] != None:
                keys.append(entry[0])
    
        return keys
  
    # Return a set consisting of the values in this map 
    def values(self):
        values = []
    
        for i in range(0, self.capacity):
            entry= self.table[i] 
            if entry[0] != None:
                values.append(entry[1])
    
        return values
                  
    # Remove all of the entries from this map 
    def clear(self):
        self.size = 0 # Reset map size
        self.capacity = DEFAULT_INITIAL_CAPACITY
        self.table = [[None,None]]*self.capacity # Reset map
        

    # Return the number of mappings in this map 
    def getSize(self):
        return self.size
        
    # Return true if this map contains no entries 
    def isEmpty(self):
        return self.size == 0
    
    # Rehash the map 
    def rehash(self):
        temp = self.items() # Get entries
        self.capacity *= 2 # Double capacity    }
        self.table = [[None,None]]*self.capacity
        self.size = 0 # Clear size
                    
        for entry in temp:
            if entry[0] != None:
                self.put(entry[0], entry[1]) # Store to new table

    # Return the entries as a string 
    def toString(self):
        return str(self.items())
    
    # Return a string representation for this map 
    def setLoadFactorThreshold(self, threshold):
        self.loadFactorThreshold = threshold

    # Return the hash table as a string 
    def getTable(self):
        return str(self.table)
    
    
    def getHash(self, hashCode):
        return hashCode & (self.capacity - 1)

def main():
    # Create a map
    map = Map()
    map.put("Smith", 30) # Add (Smith, 30 ) to map
    map.put("Anderson", 31)
    map.put("Lewis", 29)
    map.put("Cook", 29)
    map.put("Cook", 129)
    
    print("Entry set in map: " + str(map.items()))
    print("The age for Lewis is " + str(map.get("Lewis")))
    print("Is Smith in the map? " + str(map.containsKey("Smith")))
    print("Is Johnson in the map? " + 
        str(map.containsKey("Johnson")))
    print("Is value 30 in the map? " + str(map.containsValue(30)))
    print("Is value 33 in the map? " + str(map.containsValue(33)))
    print("Is age 33 in the map? " + str(map.containsValue(33)))
    print("All values for Cook? " + str(map.getAll("Cook")))
    print("keys are " + str(map.keys()))
    print("values are " + str(map.values()))

    map.remove("Smith") # Remove Smith from map
    print("The map is " + map.getTable())

    map.clear()
    print("The map is " + map.getTable())

main()