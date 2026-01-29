def water_plants(plant_list):
	try:

		print("Opening watering system")
		for plant in plant_list:
			if plant is None or plant == "":
				raise ValueError("Error: Cannot water None - invalid plant!")
			print(f"Watering {plant}")
	except ValueError as error:
		print(f"{error}")
	finally:
		print("Closing watering system (cleanup)")

def test_watering_system():
	l = ["tomato","flower", "","potato"]
	print("=== Garden Watering System ===")
	print("Testing normal watering...")
	water_plants(l)
	print("Watering completed successfully!")
	print("Testing with error...")
	water_plants(l)

test_watering_system()