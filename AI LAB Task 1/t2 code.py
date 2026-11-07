def chk_std(scr, doct, attendance, plagrisam):
    if (scr >= 70 and doct == "Complete" and attendance >= 75 and plagrisam <= 20):
        return "Pass"
    else:
        return "Fail"
tst_cases = [
    (85, "Complete", 90, 10),
    (80, "Complete", 70, 10),
    (85, "Complete", 85, 25),
    (70, "Complete", 75, 20)
]
for i, tst in enumerate(tst_cases, 1):
    scr, doct, attendance, plagrisam = tst
    result = chk_std( scr, doct, attendance, plagrisam )
    print("Test Case:", i)
    print("Input:", tst)
    print("Expected Result:", ["Pass", "Fail", "Fail", "Pass"][i-1])
    print("Obtained Result:", result)
    print("--------------------")
