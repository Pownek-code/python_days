class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass
def verify_plant_health(plant_status):
    if plant_status == "wilted" or plant_status == "sick":
        raise PlantError("The tomato plant is wilting!")

def verify_water_level(liters):
    if liters < 10:
        raise WaterError("Not enough water in the tank!")

def test_custom_errors():
    print("Custom Garden Errors Demo")

    print("Testing PlantError...")
    try:
        verify_plant_health("wilted")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    # --- Test 2: Catching WaterError specifically ---
    print("Testing WaterError...")
    try:
        verify_water_level(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("Testing catching all garden errors...")
    try:
        verify_plant_health("wilted")
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        verify_water_level(5)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    test_custom_errors()