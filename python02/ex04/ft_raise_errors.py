def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10 or water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is invalid")
    return f"Plant '{plant_name}' is healthy!"

def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    try:
        msg = check_plant_health("tomato", 5, 8)
        print(msg)
    except ValueError as e:
        print(e)

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 20, 8)
    except ValueError as e:
        print(e)