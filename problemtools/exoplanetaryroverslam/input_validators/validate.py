import sys
import re

def validate():
    lines = sys.stdin.readlines()
    if len(lines) < 2:
        sys.exit(43)
    
    # Line 0: N (must be positive integer, no leading zeros, followed by newline)
    if not re.match(r"^[1-9]\d*\n$", lines[0]):
        sys.exit(43)
    N = int(lines[0])
    
    # Line 1: M (must be positive integer, no leading zeros, followed by newline)
    if not re.match(r"^[1-9]\d*\n$", lines[1]):
        sys.exit(43)
    M = int(lines[1])
    
    if len(lines) != 2 + M + N:
        sys.exit(43)
        
    # Lines 2 to 2 + M - 1: Seeds (must be integers, no leading zeros, followed by newline)
    for i in range(2, 2 + M):
        if not re.match(r"^(0|-?[1-9]\d*)\n$", lines[i]):
            sys.exit(43)
            
    # Lines 2 + M to 2 + M + N - 1: Matrix rows
    # Must have exactly N space-separated integers, no leading/trailing spaces, exactly single spaces
    row_pattern = re.compile(rf"^(0|[1-9]\d*)( (0|[1-9]\d*)){{{N-1}}}\n$")
    
    for i in range(2 + M, 2 + M + N):
        if i == len(lines) - 1:
            # The very last line of the file might occasionally omit the trailing newline
            last_row_pattern = re.compile(rf"^(0|[1-9]\d*)( (0|[1-9]\d*)){{{N-1}}}\n?$")
            if not last_row_pattern.match(lines[i]):
                sys.exit(43)
        else:
            if not row_pattern.match(lines[i]):
                sys.exit(43)
                
    sys.exit(42)

if __name__ == '__main__':
    validate()
