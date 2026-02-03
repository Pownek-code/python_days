import time
def stream_game_events(n):
    names = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up", "died", "joined guild"]
    
    for i in range(1, n + 1):
        player_idx = i % len(names)
        action_idx = (i * 3) % len(actions)
        level = (i * 7) % 20 + 1
        
        event = {
            "id": i,
            "player": names[player_idx],
            "action": actions[action_idx],
            "level": level
        }
        yield event

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def prime_generator(limit):
    """
    Generates the first 'limit' prime numbers.
    """
    num = 2
    count = 0
    while count < limit:
        # Check if prime
        is_prime = True
        # Simple primality test
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield num
            count += 1
        num += 1
def main():
    print("=== Game Data Stream Processor ===")
    
    total_events = 1000
    print(f"Processing {total_events} game events...")
    stats = { "high_level": 0, "treasure": 0, "levelup": 0 }
    start_time = time.time()
    for event in stream_game_events(total_events):
        if event['id'] <= 3:
            print(f"Event {event['id']}: Player {event['player']} (level {event['level']}) {event['action']}")
        if event['level'] >= 10: stats["high_level"] += 1
        if event['action'] == "found treasure": stats["treasure"] += 1
        elif event['action'] == "leveled up": stats["levelup"] += 1
    end_time = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['levelup']}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):")
    fib_gen = fibonacci_generator(10) 
    try:
        first = next(fib_gen) 
        print(f"{first}", end="")
        while True:
            val = next(fib_gen)
            print(f", {val}", end="")
    except StopIteration:
        print()
    print("Prime numbers (first 5):")
    prime_gen = prime_generator(5)
    p1 = next(prime_gen)
    p2 = next(prime_gen)
    p3 = next(prime_gen)
    p4 = next(prime_gen)
    p5 = next(prime_gen)
    print(f"{p1}, {p2}, {p3}, {p4}, {p5}")
if __name__ == "__main__":
    main()