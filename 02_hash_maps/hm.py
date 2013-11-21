"""
HashMap Table Implementation
@jlengrand
2013/11
"""

class HashMap():
	def __init__(self, hash_size=513):
		self._hash_size = hash_size
		self._size = 0
		self.hmap = [0] * self._hash_size
		
	def add(self, value):
		"""
		Adds the provided value to the hashmap.
		Raises an Exception if a collision is detected
		"""
		key = self._hash(value)
		if self.hmap[key] == 0:
			self.hmap[key] = value
			self._size += 1
		else: 
			raise Exception("Collision detected at index %d", key)
	
		# TODO: Keep implementing
	
	def size(self):
		return self._size
	
	def _hash(self, value):
		"""
		Generates a hash for the given value.
		The input is expected to be a String, with only ASCII characters.
		"""
		if len(value) < 1:
			raise Exception("Size of value must be greater than one")
		
		# hash function taken from HT3.
		# We shift and add : << 4 is a *16
		h = 0
		for letter in value:
			h = (h << 4) + ord(letter)
			
		return h % self._hash_size

	