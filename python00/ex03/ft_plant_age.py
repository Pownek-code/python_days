def ft_plant_age():
	age = int(input("Enter plant age in days: "))
	print(f"{"Plant is ready to harvest!" if age > 60 else "Plant needs more time to grow."}")