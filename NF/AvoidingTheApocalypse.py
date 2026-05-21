import sys
import collections

def main():
    # Read in input data all at once and iterate over it
    input_data = sys.stdin.read().split()

    # Pointer to current position in input data
    ptr = 0

    num_test_cases = int(input_data[ptr])
    ptr += 1
    
    # Infinity constant for unbounded capacities
    INF = 10**15
    
    # Loop through each test case
    for _ in range(num_test_cases):

        # Break if we run out of input data
        if ptr >= len(input_data):
            break
        
        # Read in variables for this test case
        # n is the number of locations
        n = int(input_data[ptr])
        ptr += 1

        # i_start: starting location
        # g: number of people in our group
        # s_max: max time steps allowed
        i_start, g, s_max = map(int, input_data[ptr:ptr+3])
        ptr += 3

        # m: number of medical facilities
        m = int(input_data[ptr])
        ptr += 1

        medical_facilities = []
        for _ in range(m):
            medical_facilities.append(int(input_data[ptr]))
            ptr += 1
        
        # r: number of roads
        r = int(input_data[ptr])
        ptr += 1
        
        roads = []
        for _ in range(r):
            u, v, p, t = map(int, input_data[ptr:ptr+4])
            ptr += 4
            roads.append((u, v, p, t))

        # Time-expanded graph setup
        # Instead of dealing with time as a cost, we make a copied "layer" of the graph
        # for every single time step from 0 up to s_max.
        
        # Helper function to map (location, timestep) to a unique node ID
        # locations are 1 to n. time is 0 to s_max.
        def node_id(loc, time):
            return loc + time * n
            
        total_nodes = n * (s_max + 1)
        source = 0
        sink = total_nodes + 1
        
        # Simple adjacency list: [to_node, capacity, reverse_edge_index]
        graph = [[] for _ in range(sink + 1)]
        
        def add_edge(u, v, cap):
            graph[u].append([v, cap, len(graph[v])])
            graph[v].append([u, 0, len(graph[u]) - 1])
            
        # 1. Start Node: Connect Super-Source to our starting location at time 0
        # The capacity is 'g', because we only have 'g' people in our group.
        add_edge(source, node_id(i_start, 0), g)
        
        # 2. Wait Edges: Allow people to stay at the same location for 1 time step
        # Infinite capacity because any number of people can wait.
        for loc in range(1, n + 1):
            for t in range(s_max):
                add_edge(node_id(loc, t), node_id(loc, t + 1), INF)
                
        # 3. Travel Edges: Crossing roads takes 't_cross' time.
        # So we connect location 'u' at time 't' to location 'v' at time 't + t_cross'
        # The capacity is 'p' because only 'p' people can enter per timestep.
        for u, v, p, t_cross in roads:
            for t in range(s_max - t_cross + 1):
                add_edge(node_id(u, t), node_id(v, t + t_cross), p)
                
        # 4. Sink Edges: Connect any medical facility at any timestep to the Super-Sink
        for mf in medical_facilities:
            for t in range(s_max + 1):
                add_edge(node_id(mf, t), sink, INF)
                
        # Edmonds-Karp using BFS
        total_people = 0
        
        while True:
            # 1. Breadth-First Search (BFS) to find ANY path with available capacity
            parent_node = [-1] * (sink + 1)
            parent_edge = [-1] * (sink + 1)
            visited = [False] * (sink + 1)
            
            queue = collections.deque([source])
            visited[source] = True
            
            reached_sink = False
            while queue:
                u = queue.popleft()
                
                if u == sink:
                    reached_sink = True
                    break
                    
                for i, edge in enumerate(graph[u]):
                    v, cap, rev = edge
                    if not visited[v] and cap > 0:
                        visited[v] = True
                        parent_node[v] = u
                        parent_edge[v] = i
                        queue.append(v)
            
            # If sink couldn't be reached, all flow has been pushed
            if not reached_sink:
                break
                
            # 2. Find the bottleneck capacity along the path we just found
            path_cap = INF
            curr = sink
            while curr != source:
                p_node = parent_node[curr]
                idx = parent_edge[curr]
                path_cap = min(path_cap, graph[p_node][idx][1])
                curr = p_node
                
            # 3. Push the flow down the path and update the residual graph
            total_people += path_cap
            curr = sink
            while curr != source:
                p_node = parent_node[curr]
                idx = parent_edge[curr]
                rev_idx = graph[p_node][idx][2]
                
                # Decrease forward capacity
                graph[p_node][idx][1] -= path_cap
                # Increase reverse capacity
                graph[curr][rev_idx][1] += path_cap
                
                curr = p_node
                
        # Output the max flow
        print(total_people)

if __name__ == "__main__":
    main()
