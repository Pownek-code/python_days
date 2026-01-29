class SecurePlant:
	def __init__(self, name: str, height: int, age: int):
		self._name = name
		self._height = 0
		self._age = 0

		self.set_height(height)
		self.set_age(age)
	def  set_height(self, height : int) -> int:
		if height < 0:
			print("Error")
		else:
			self._height = height
	def set_age(self, age: int) -> int:
		if age < 0:
			print("Error")
		else:
			self._age = age
	def __str__(self):
		return f"{self._name}, {self._height}, {self._age}"

if __name__ == "__main__":
	p = SecurePlant("Rose", 23, 44)
	print(p)


