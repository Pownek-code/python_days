class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def __str__(self):
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = (self.height * self.trunk_diameter) // 300
        print(f"{self.name} provides {shade_area} square meters of shade")

    def __str__(self):
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter"

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest"

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    rose.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    oak.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(tomato)
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print()
    daisy = Flower("Daisy", 15, 10, "white")
    pine = Tree("Pine", 300, 800, 30)
    carrot = Vegetable("Carrot", 10, 45, "spring", "vitamin A")
    for p in [daisy, pine, carrot]:
        print(p)	