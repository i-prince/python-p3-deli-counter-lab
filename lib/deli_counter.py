def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}. You are number {position} in line.")

def line(line):
    if not line:
        print("The line is currently empty.")
    else:
        positions = [f"{index + 1}. {name}" for index, name in enumerate(line)]
        print("The line is currently: " + " ".join(positions))

def now_serving(line):
    if not line:
        print("There is nobody waiting to be served!")
    else:
        serving = line.pop(0)
        print(f"Currently serving {serving}.")
