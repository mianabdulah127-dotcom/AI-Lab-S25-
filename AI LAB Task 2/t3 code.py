previous_mode = "None"
def chk_tmp(tmp, occupancy):
    global previous_mode
    if occupancy == "Empty":
        goal = "OFF"
    elif tmp >= 30:
        goal = "COOL"
    elif tmp <= 18:
        goal = "HEAT"
    else:
        goal = "FAN"
    if goal == previous_mode:
        command = "No Command"
    else:
        command = "Send Command"
    previous_mode = goal
    return goal, command
tst_cases = [
    (32, "Occupied"),
    (32, "Occupied"),
    (30, "Occupied"),
    (18, "Occupied"),
    (15, "Occupied"),
    (25, "Empty")
]
for i, tst in enumerate(tst_cases, 1):
    old_mode = previous_mode
    tmp, occupancy = tst
    goal, command = chk_tmp(tmp, occupancy)
    print("Test:", i)
    print("Previous Mode:", old_mode)
    print("Percept:", tst)
    print("Target:", goal)
    print("Command:", command)
    print("-------------------")
