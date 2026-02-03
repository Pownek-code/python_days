def ft_seed_inventory(seed_type: str, quantity: int, unit: int) -> None:
    seed = seed_type.capitalize
    if ("packets" == unit):
        print(f"{seed} seeds: {quantity} packets available")
    elif ("grams" == unit):
        print(f"{seed} seeds: {quantity} grams available")
    elif ("area" == unit):
        print(f"{seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
