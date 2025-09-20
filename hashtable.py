class HashTable:
    def __init__(self, size=50):
        """
        Initializes the hash table with a specified size.
        The table is a list of lists, where each inner list serves as a "bucket"
        or "chain" for collision handling.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        A simple hash function. It uses Python's built-in hash() for the key
        and then uses the modulo operator to ensure the hash index fits within
        the table's size. This gives us a valid index.
        """
        return hash(key) % self.size

    def set_value(self, key, value):
        """
        Adds a key-value pair to the hash table.
        It handles collisions by appending to the correct bucket's list.
        """
        # Get the hash index for the key
        hash_index = self._hash(key)

        # Get the bucket (the list) at that index
        bucket = self.table[hash_index]

        # Check if the key already exists in the bucket's list
        # If it does, we update the value.
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i] = (key, value)
                return

        # If the key is new, add the key-value pair to the end of the bucket's list.
        # This is how separate chaining handles collisions.
        bucket.append((key, value))

    def get_value(self, key):
        """
        Retrieves the value associated with a given key.
        Searches the bucket's list for the correct key.
        """
        # Get the hash index
        hash_index = self._hash(key)

        # Get the bucket
        bucket = self.table[hash_index]

        # Search the bucket's list for the key
        for pair in bucket:
            if pair[0] == key:
                return pair[1]  # Return the value
        
        # Key not found
        return None

    def delete_value(self, key):
        """
        Deletes a key-value pair from the hash table.
        """
        # Get the hash index
        hash_index = self._hash(key)
        
        # Get the bucket
        bucket = self.table[hash_index]
        
        # Find the key in the bucket's list and remove it
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True # Deletion successful
        
        return False # Key not found

    def __str__(self):
        """
        A string representation to visualize the hash table.
        """
        output = ""
        for i, bucket in enumerate(self.table):
            if bucket:
                output += f"Bucket {i}: {bucket}\n"
        return output

# --- Example Usage ---
my_hash_table = HashTable(size=10)

# 1. Setting values
print("Setting values:")
my_hash_table.set_value("name", "Alice")
my_hash_table.set_value("age", 30)
my_hash_table.set_value("city", "New York")
print(my_hash_table)

# 2. Demonstrating collision handling
# For demonstration, let's say "name" and "race" have the same hash index.
# In this case, both "name" and "race" will be in the same bucket's list.
print("\nDemonstrating a potential collision:")
my_hash_table.set_value("race", "Human")
print(my_hash_table)

# 3. Getting a value
print(f"\nGetting value for 'age': {my_hash_table.get_value('age')}")
print(f"Getting value for 'city': {my_hash_table.get_value('city')}")

# 4. Updating a value
print("\nUpdating 'age' from 30 to 31:")
my_hash_table.set_value("age", 31)
print(f"New age: {my_hash_table.get_value('age')}")

# 5. Deleting a value
print("\nDeleting 'city':")
my_hash_table.delete_value("city")
print(my_hash_table)