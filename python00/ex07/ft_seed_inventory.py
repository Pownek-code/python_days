def ft_seed_inventory(seed_type: str, quantity: int, unit: int) -> None:
	if ("packets" == unit):
		print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
	elif ("grams" == unit):
		print(f"{seed_type.capitalize()} seeds: {quantity} grams available")
	elif ("area" == unit):
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
