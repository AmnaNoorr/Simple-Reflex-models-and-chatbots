import random

def reflex_vacuum_agent_3sq(location, status):
    """Simple reflex agent function for the three-square (A, B, C) vacuum world."""
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    elif location == "B":
        # At B, if clean, pick a direction to continue exploring
        return random.choice(["Left", "Right"])
    else:  # location == "C"
        return "Left"

def run_vacuum_world_3sq(steps=10):
    env = {
        "A": random.choice(["Clean", "Dirty"]),
        "B": random.choice(["Clean", "Dirty"]),
        "C": random.choice(["Clean", "Dirty"])
    }
    location = random.choice(["A", "B", "C"])
    performance = 0

    print("Initial State of the environment:", env)
    print(f"Vacuum randomly placed at Location {location}.\n" + "-"*40)

    for step in range(1, steps + 1):
        status = env[location]
        action = reflex_vacuum_agent_3sq(location, status)
        print(f"Step {step}: Vacuum is at [{location}] | Status: {status}")

        if action == "Suck":
            env[location] = "Clean"
            performance += 1
            print(f"  -> Action: Sucked dirt at Location {location}.\n")
        elif action == "Right":
            if location == "A":
                location = "B"
            elif location == "B":
                location = "C"
            print(f"  -> Action: Moved Right to Location {location}.\n")
        elif action == "Left":
            if location == "C":
                location = "B"
            elif location == "B":
                location = "A"
            print(f"  -> Action: Moved Left to Location {location}.\n")

        # Terminate early if all squares are clean
        if env["A"] == "Clean" and env["B"] == "Clean" and env["C"] == "Clean":
            print("All locations (A, B, C) are clean! Stopping early.")
            break

    print("-" * 40)
    print("Final Environment State:", env)
    print("Performance Measurement (Dirt Cleaned):", performance)

# Run simulation
run_vacuum_world_3sq()