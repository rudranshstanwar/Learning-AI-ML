with open("Sample.txt", "r") as f:
    for i in range(0, 4):
        line = f.readline()
        if "python" in line:
            print("Found")
            break