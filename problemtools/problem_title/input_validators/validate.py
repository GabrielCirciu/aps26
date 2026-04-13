import sys
import re

# Based on my kattis work, this is where an input is verified to be usable

def validate():
    lines = sys.stdin.readlines()
    if not lines:
        sys.exit(43)
    
    # Check first line: N M T (Nodes, Edges, Type)
    if not re.match(r"^\d+ \d+ [12]\n$", lines[0]):
        sys.exit(43)
    
    first_line = lines[0].split()
    M = int(first_line[1])
    
    # Ensure there are exactly M edge lines following
    if len(lines) != M + 1:
        sys.exit(43)
        
    for i in range(1, M + 1):
        if not re.match(r"^\d+ \d+ \d+\n$", lines[i]):
            sys.exit(43)
            
    sys.exit(42)

validate()