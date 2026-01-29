import sys

def main():
    # 1. Parse Input: "item:quantity" -> Dictionary
    # Example input: sword:1 potion:5 shield:2 armor:3 helmet:1
    inventory = {}
    
    # Skip script name, iterate over args
    for arg in sys.argv[1:]:
        try:
            if ':' in arg:
                key, value = arg.split(':')
                inventory[key] = int(value)
        except ValueError:
            print(f"Skipping invalid item: {arg}")
    print("=== Inventory System Analysis ===")
    total_items = 0
    for qty in inventory.values():
        total_items += qty
    unique_items = len(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print("=== Current Inventory ===")
    for item, qty in inventory.items():
        percent = (qty / total_items) * 100 if total_items > 0 else 0
        print(f"{item}: {qty} units ({percent:.1f}%)")
    print("=== Inventory Statistics ===")
    
    if inventory:
        most_abundant_item = ""
        most_abundant_qty = -1
        least_abundant_item = ""
        least_abundant_qty = total_items + 1
        for item, qty in inventory.items():
            if qty > most_abundant_qty:
                most_abundant_qty = qty
                most_abundant_item = item
            if qty < least_abundant_qty:
                least_abundant_qty = qty
                least_abundant_item = item
        print(f"Most abundant: {most_abundant_item} ({most_abundant_qty} units)")
        print(f"Least abundant: {least_abundant_item} ({least_abundant_qty} units)")
    print("=== Item Categories ===")
    categories = {
        'Moderate': {},
        'Scarce': {}
    }
    for item, qty in inventory.items():
        if qty >= 5:
            categories['Moderate'][item] = qty
        else:
            categories['Scarce'][item] = qty
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")
    print("=== Management Suggestions ===")
    restock_list = []
    for item, qty in inventory.items():
        if qty < 2:
            restock_list.append(item)
    print(f"Restock needed: {restock_list}")
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    
    search_item = 'sword'
    is_present = search_item in inventory
    print("Sample lookup")
    print(f"'{search_item}' in inventory: {is_present}")

if __name__ == "__main__":
    main()