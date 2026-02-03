class Plant:
    counter = 0
    def __init__(self, name: str, starting_height: str, starting_age: str):
        self.name = name
        self.height = starting_height
        self.age = starting_age
        Plant.counter += 1
    def __str__(self):
        return f"{self.name}, {self.height}, {self.age}"
	
if __name__ == '__main__':
    order = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90), ("Sunflower", 80, 45)
		  ,("Fern", 15, 120)]
	
    for name, height, age in order:
        new = Plant(name, height, age)
        print(new)

print(f"{Plant.counter}")
