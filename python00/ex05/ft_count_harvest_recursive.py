def ft_count_harvest_recursive():
    inp = int(input("Days until harvest: "))
    recursion(inp)
    print("Harvest time!")


def recursion(time):
    if (time > 1):
        recursion(time - 1)
    print(f"Day {time}")
