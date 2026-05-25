import json
import math
import csv

test_files = [
    "data1.json","test_case_1.json", "test_case_2.json", "test_case_3.json", "test_case_4.json",
    "test_case_5.json", "test_case_6.json", "test_case_7.json", "test_case_8.json",
    "test_case_9.json", "test_case_10.json"
]

# JSON parsing
for test_file in test_files:
    print(f"\nRunning {test_file}")

    try:
        with open(test_file, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f" File not found: {test_file}")
        continue

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    # Initialize report
    report = {
        agent_id: {
            "packages_delivered": 0,
            "total_distance": 0.0
        }
        for agent_id in agents
    }

    # Distance calculation
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    # Agent-package assignment
    for pkg in packages:
        wh_location = warehouses[pkg["warehouse"]]

        min_distance = float("inf")
        nearest_agent = None

        for agent_id in agents:
            d = distance(agents[agent_id], wh_location)

            if d < min_distance:
                min_distance = d
                nearest_agent = agent_id

        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += (distance(agents[nearest_agent], wh_location) + distance(wh_location, pkg["destination"]))

    # Validate all packages delivered
    total_delivered = 0

    for agent_id in report:
        total_delivered += report[agent_id]["packages_delivered"]

    assert total_delivered == len(packages)

    print(f" Test passed: {total_delivered} packages delivered")


    # Calculate efficiency + best agent
    best_agent = None
    best_efficiency = float("inf")

    for agent in report:
        stats = report[agent]

        if stats["packages_delivered"] > 0:
            efficiency = stats["total_distance"] / stats["packages_delivered"]
        else:
            efficiency = 0

        stats["total_distance"] = round(stats["total_distance"], 2)
        stats["efficiency"] = round(efficiency, 2)

        if efficiency < best_efficiency and stats["packages_delivered"] > 0:
            best_efficiency = efficiency
            best_agent = agent

    report["best_agent"] = best_agent


    # Simulation & report
    output_file = f"report_{test_file.replace('.json', '')}.json"
    with open(output_file, "w") as f:
        json.dump(report, f, indent=4)


    # Export top performer to CSV getting data from test_case_10.json(BONUS TASK)
    with open("top_agent.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Agent ID", "Packages Delivered", "Total Distance"])
        writer.writerow([
            best_agent,
            report[best_agent]["packages_delivered"],
            report[best_agent]["total_distance"]
        ])
