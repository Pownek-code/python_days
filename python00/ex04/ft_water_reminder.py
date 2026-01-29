def ft_water_reminder():
	print(f"{"Water the plants!" if int(input("Days since last watering:")) > 2 else "Plants are fine"}")