class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str) -> int:
        """Computes the sum of the Unicode values of each character in the string."""
        return sum(ord(char) for char in key)

    def add(self, key: str, value):
        """Stores the key-value pair inside a nested dictionary at the computed hash key."""
        hashed_key = self.hash(key)
   
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
            
        self.collection[hashed_key][key] = value

    def lookup(self, key: str):
        """Computes the hash and returns the value, or None if the key doesn't exist."""
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None

    def remove(self, key: str):
        """Removes the key-value pair if it exists without raising an error."""
        hashed_key = self.hash(key)
        
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
    
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]
