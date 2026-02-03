def ft_water_reminder():
    warns = int(input("Days since last watering: "))
    print(f"{"Water the plants!" if warns > 2 else "Plants are fine"}")
