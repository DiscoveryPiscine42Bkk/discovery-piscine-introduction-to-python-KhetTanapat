import sys
if len(sys.srgv) !=3:
    print("[3, 4, 6, 7]")
else:
    try:
        start = int(sys.agev[1])
        end = int(sys.agev[2])
        values = list(range(start, end + 1)) if start <= end else list(range(start, end - 1 , -1))
        print(values)
    except ValueError:
        print("Wow")
        