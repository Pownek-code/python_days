class Plant:
	def __init__(self ,name: str, height: int, age: int):
		self.name = name
		self.height = height
		self.age = age
	def __str__(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

def main():
	print(Plant("Rose", 5, 3))
	print(Plant("ophelia", 2, 5))
	print(Plant("darwin", 7, 2))

if __name__ == "__main__":
	main()
# 	print(Plant("Rose", 5, 3))
# 	print(Plant("ophelia", 2, 5))
# 	print(Plant("darwin", 7, 2))

