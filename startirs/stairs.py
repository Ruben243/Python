def draw_stairs(stairs):
    if stairs > 0:
        for stair in range(stairs + 1):
            spaces = "  " * (stairs - stair)
            stair_draw = "_" if stair == 0 else "_|"
            print(f"{spaces}{stair_draw}")

    elif stairs < 0:
        for stair in range(abs(stairs) + 1):
            stair_draw = "_" if stair == 0 else "|_"
            spaces = " " * (stair * 2 - 1)
            print(f"{spaces}{stair_draw}")
    else:
        print("__")
        
        
draw_stairs(4)
draw_stairs(-4)