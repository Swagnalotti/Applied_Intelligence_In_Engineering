TODAY = "Wednesday"
PI = 3.1415926535897932346264338979323

def function1():
    print(f"Today is: {TODAY}")

def function2():
    today = "Thursday"
    print(f"Today is: {today}")

def function3():
    global TODAY
    TODAY = "Friday"

function3()
print(f"Today is: {TODAY}")
function1()
function2()