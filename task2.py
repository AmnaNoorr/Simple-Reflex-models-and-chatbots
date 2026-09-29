def reflex_vacuum_agent_3sq(location, status):
    """
    Pure Simple Reflex Agent for 3 locations (A, B, C).
    Decides action strictly based on current (location, status) percept.
    No memory or internal state is maintained.
    """
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        return "Right"  # Traversal pattern: A -> B -> C -> B -> A
    elif location == "C":
        return "Left"

def main():
    print("=== VACUUM WORLD SETUP ===")
    
    # 1. Get initial environment state from user runtime input
    env = {}
    for loc in ["A", "B", "C"]:
        while True:
            val = input(f"Enter status for Location {loc} (Clean/Dirty): ").strip().capitalize()
            if val in ["Clean", "Dirty"]:
                env[loc] = val
                break
            print("Invalid input! Please type 'Clean' or 'Dirty'.")

    # 2. Get starting location from user runtime input
    while True:
        location = input("Enter starting location (A, B, or C): ").strip().upper()
        if location in ["A", "B", "C"]:
            break
        print("Invalid input! Please type 'A', 'B', or 'C'.")

    # 3. Get total steps to run
    while True:
        try:
            steps = int(input("Enter number of simulation steps to run (e.g., 6 or 10): "))
            if steps > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    performance = 0

    print("\n" + "="*45)
    print("INITIAL ENVIRONMENT STATE:", env)
    print(f"VACUUM INITIAL LOCATION: {location}")
    print("="*45 + "\n")

    # Simulation execution
    for step in range(1, steps + 1):
        # Read current percept strictly at runtime
        status = env[location]
        
        # Simple Reflex decision based ONLY on current percept
        action = reflex_vacuum_agent_3sq(location, status)

        print(f"Step {step}: Vacuum is at [{location}] | Status: {status}")

        # Execute action in environment
        if action == "Suck":
            env[location] = "Clean"
            performance += 1
            print(f"  -> Action: Sucked dirt at Location {location}.\n")
        elif action == "Right":
            old_loc = location
            if location == "A":
                location = "B"
            elif location == "B":
                location = "C"
            print(f"  -> Action: Moved Right from {old_loc} to {location}.\n")
        elif action == "Left":
            old_loc = location
            if location == "C":
                location = "B"
            elif location == "B":
                location = "A"
            print(f"  -> Action: Moved Left from {old_loc} to {location}.\n")

    print("="*45)
    print("FINAL ENVIRONMENT STATE:", env)
    print("PERFORMANCE (Total Dirt Cleaned):", performance)
    print("="*45)

if __name__ == "__main__":
    main()
    