import sys

def main():
    score = 0
    # Kattis judge outputs "verdict points" for each test case to the grader
    for line in sys.stdin:
        try:
            parts = line.split()
            if not parts: continue
            verdict, points = parts[0], parts[1]
            if verdict == 'AC':
                score += float(points)
        except Exception:
            continue
    
    # Output "AC score" to the judge to set the final verdict/points
    print(f"AC {score}")

if __name__ == '__main__':
    main()
