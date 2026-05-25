# Python Assignment 

Python Assignment: Mystery Delivery System <br>


## Overview
This project simulates package delivery operations for a logistics company using multiple warehouses and delivery agents.  
For each test case, a report is generated that includes:

1. Packages delivered by each agent  
2. Total distance traveled  
3. Delivery efficiency  
4. Best performing agent
5. Bonus Task- Export Top Performer to CSV
   

## Entities

- **Warehouses:** W1, W2, W3  
- **Agents:** A1, A2, A3  
- **Packages:** p1, p2, p3, p4, p5  

## Distance Calculation

Euclidean distance formula is used:
    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

## Nearest Agent Selection

For each package:

1. Distance is calculated from all agents to the package’s warehouse  
2. The agent with the minimum distance is assigned  

Example result:
- W1 -> A1  
- W2 -> A2  
- W3 -> A3  

## Total Distance Calculation

1. For each package: <br>
       Package Distance = Distance(agent → warehouse) + Distance(warehouse → destination)

2. Agent-wise total distance: <br>
       Total Distance = Sum of all package distances delivered by the agent


## Efficiency Calculation
Efficiency = Total Distance / Number of Packages Delivered

## Best Agent Selection
The best agent is the agent with the **lowest efficiency**.

## Output Report
For each test case, a JSON report file is generated.

## Bonus Task — Export Top Performer to CSV

1. Uses data from report_test_case_10.json
2. Identifies the best_agent 
3. Exports agent details to a CSV file  

