class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        print("Adding plants to garden...")
        if plant_name is None or plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant} -> success")
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if water_level > 10 or water_level < 1:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        
        # Validate Sun
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours} is invalid")
        
        print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

def test_garden_management():
    print("=== Garden Management System ===")
    manager = GardenManager()
    plants_to_add = ["tomato", "lettuce", ""] 
    
    for plant in plants_to_add:
        try:
            manager.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print()
    manager.water_plants()
    print()
    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
    except GardenError as e:
        print(e)
    try:
        manager.check_plant_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")
    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")

if __name__ == "__main__":
    test_garden_management()