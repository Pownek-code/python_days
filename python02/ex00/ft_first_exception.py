def check_temperature(temp_str: str) -> None:
	try:
		data = (int)(temp_str)
		if data > 40:
			print(f"Error: {data}°C is too hot for plants (max 40°C)")
		elif data < 0:
			print(f"Error: {data}°C is too cold for plants (min 0°C)")
		else:
			print(f"Temperature {data}°C is perfect for plants!")
	except ValueError:
		print(f"Error: {temp_str} is not a valid number")
def test_temperature_input():
	print("Testing temperature: 25")
	check_temperature("25")
	print("Testing temperature: abc")
	check_temperature("abc")
	print("Testing temperature: 100")
	check_temperature("100")
	print("Testing temperature: -50")
	check_temperature("-50")
	print("All tests completed - program didn't crash!")
if __name__ == "__main__":
	test_temperature_input()
