import sys, math

def calculate_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    sq_diff = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    return math.sqrt(sq_diff)

def test_coordinate_system():
    print("=== Game Coordinate System ===")
    my_position = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {my_position}")
    dist = calculate_distance(origin, my_position)
    print(f"Distance between {origin} and {my_position}: {dist:.2f}")
    input_str = "3,4,0"
    print(f'Parsing coordinates: "{input_str}"')
    try:
        parts = input_str.split(',')
        parsed_pos = (int(parts[0]), int(parts[1]), int(parts[2]))
        print(f"Parsed position: {parsed_pos}")
        dist_parsed = calculate_distance(origin, parsed_pos)
        print(f"Distance between {origin} and {parsed_pos}: {dist_parsed:.1f}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    bad_input = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_input}"')
    try:
        bad_parts = bad_input.split(',')
        bad_pos = (int(bad_parts[0]), int(bad_parts[1]), int(bad_parts[2]))
        print(bad_pos)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print("Unpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x} Y={y} Z={z}")

if __name__ == "__main__":
    test_coordinate_system()