"""
search.py

Students must implement TODO sections.
Includes: BFS, DFS, UCS, A* (with Manhattan & Euclidean heuristics).
"""

from collections import deque
import heapq
import math
import time

# ---------------------
# BFS
# ---------------------
def breadth_first_search(start, goal, neighbors_fn):
    if start == goal:
        return [start]
    
    start_time = time.time()
    
    fringe = deque([(start, [start])])
    explored = set()
    
    while fringe:
        Node, path = fringe.popleft()
        
        if Node in explored:
            continue

        explored.add(Node)
        
        for neighbor in neighbors_fn(Node):
            if neighbor not in explored :
                if neighbor == goal:
                    end_time = time.time()
                    print(f"BFS - Nodes expanded: {len(explored)}")
                    print(f"BFS - Path length: {len(path) + 1}")
                    print(f"BFS - Time: {(end_time - start_time)*1000:.2f} ms")
                    return path + [neighbor]
                
                fringe.append((neighbor, path + [neighbor]))
    
    end_time = time.time()
    print(f"BFS - No path found! Nodes expanded: {len(explored)}")
    print(f"BFS - Time: {(end_time - start_time)*1000:.2f} ms")
    return []


# ---------------------
# DFS
# ---------------------
def depth_first_search(start, goal, neighbors_fn):
    if start == goal:
        return [start]
    
    start_time = time.time()
    
    fringe = [(start, [start])]  
    explored_path = {}
    
    while fringe:
        Node, path = fringe.pop()

        explored_path[Node]=path
        
        for neighbor in neighbors_fn(Node):
            if neighbor not in path  :
                if neighbor == goal:
                    end_time = time.time()
                    print(f"DFS - Nodes explored_path: {len(explored_path)}")
                    print(f"DFS - Path length: {len(path) + 1}")
                    print(f"DFS - Time: {(end_time - start_time)*1000:.2f} ms")
                    return path + [neighbor]
                
                fringe.append((neighbor, path + [neighbor]))
    
    end_time = time.time()
    print(f"DFS - No path found! Nodes explored_path: {len(explored_path)}")
    print(f"DFS - Time: {(end_time - start_time)*1000:.2f} ms")
    return []


# ---------------------
# UCS
# ---------------------
def uniform_cost_search(start, goal, neighbors_fn):
    if start == goal:
        return [start]
    
    start_time = time.time()
    
    counter = 0
    fringe = [(0, counter, start, [start])]
    explored = {}
    
    while fringe:
        cost, _, Node, path = heapq.heappop(fringe)
        
        if Node in explored:
            continue
        
        explored[Node] = cost

        if Node == goal:
            end_time = time.time()
            print(f"UCS - Nodes expanded: {len(explored)}")
            print(f"UCS - Total cost: {cost}")
            print(f"UCS - Path length: {len(path)}")
            print(f"UCS - Time: {(end_time - start_time)*1000:.2f} ms")
            return path

        for neighbor, step_cost in neighbors_fn(Node):
            if neighbor not in explored:
                new_cost = cost + step_cost
                counter += 1
                heapq.heappush(fringe, (new_cost, counter, neighbor, path + [neighbor]))
    
    end_time = time.time()
    print(f"UCS - No path found! Nodes expanded: {len(explored)}")
    print(f"UCS - Time: {(end_time - start_time)*1000:.2f} ms")
    return []


# ---------------------
# A* Search
# ---------------------
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    #pass

def a_star_search(start, goal, neighbors_fn, heuristic="manhattan"):
    if start == goal:
        return [start]
    
    start_time = time.time()
    
    if heuristic == "manhattan":
        h_cost = manhattan
    else:
        h_cost = euclidean
    
    g_cost = {start: 0}
    counter = 0
    fringe = [(h_cost(start, goal),counter, start, [start])]  
    explored = {}
    
    while fringe:
        cost, _,Node, path = heapq.heappop(fringe)
        
        if Node in explored:
            continue

        explored[Node] = cost
        
        if Node == goal:
            end_time = time.time()
            print(f"A* ({heuristic}) - Nodes expanded: {len(explored)}")
            print(f"A* ({heuristic}) - Total cost: {g_cost[Node]}")
            print(f"A* ({heuristic}) - Path length: {len(path)}")
            print(f"A* ({heuristic}) - Time: {(end_time - start_time)*1000:.2f} ms")
            return path
        
        for neighbor, step_cost in neighbors_fn(Node):
            if neighbor in explored:
                continue
            else : 
                g_cost[neighbor] = g_cost[Node] + step_cost
                f_cost = g_cost[neighbor] + h_cost(neighbor, goal)
                counter -=1
                heapq.heappush(fringe, (f_cost,counter, neighbor, path + [neighbor]))
            
    end_time = time.time()
    print(f"A* ({heuristic}) - No path found! Nodes expanded: {len(explored)}")
    print(f"A* ({heuristic}) - Time: {(end_time - start_time)*1000:.2f} ms")
    return []