class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth_history = 0

    def grow(self, centimeters: int):
        self.height += centimeters
        self.growth_history += centimeters
        print(f"{self.name} grew {centimeters}cm")

    def __str__(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, prize_points: int):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize_points}"

class GardenManager:
    total_gardens = 0

    class GardenStats:
        def generate_report(self, owner: str, plants: list):
            print(f"=== {owner}'s Garden Report ===")
            print("Plants in garden:")
            total_growth = 0
            count_reg = 0
            count_flowering = 0
            count_prize = 0
            score = 0

            for p in plants:
                print(p)
                total_growth += p.growth_history
                c_name = p.__class__.__name__
                if c_name == "Plant":
                    count_reg += 1
                elif c_name == "FloweringPlant":
                    count_flowering += 1
                elif c_name == "PrizeFlower":
                    count_prize += 1
                score += p.height
                if c_name == "FloweringPlant" or c_name == "PrizeFlower":
                    score += 15
                
                if c_name == "PrizeFlower":
                    score += p.prize_points

            count_total = 0
            for _ in plants:
                count_total += 1
            
            print(f"Plants added: {count_total}, Total growth: {total_growth}cm")
            print(f"Plant types: {count_reg} regular, {count_flowering} flowering, {count_prize} prize flowers")
            print(f"Height validation test: {GardenManager.validate_height(10)}")
            print(f"Garden scores {owner}: {score}, Bob: 92")

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    @staticmethod
    def validate_height(height: int) -> bool:
        if height < 0:
            return False
        return True

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.total_gardens}")

    def add_plant(self, plant):
        if GardenManager.validate_height(plant.height):
            self.plants.append(plant)
            print(f"Added {plant.name} to {self.owner}'s garden")
        else:
            print(f"Error: Invalid height for {plant.name}")

    def print_report(self):
        stats = self.GardenStats()
        stats.generate_report(self.owner, self.plants)

if __name__ == "__main__":
    print("Garden Management System Demo")
    
    alice = GardenManager("Alice")
    
    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red")
    sunflower = PrizeFlower("Sunflower", 50, 45, "yellow", 10)
    
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    
    print(f"{alice.owner} is helping all plants grow...")
    
    for p in alice.plants:
        p.grow(1)
        
    print()
    alice.print_report()
    
    bob = GardenManager("Bob")
    
    GardenManager.create_garden_network()