name = "Dave"  # global
count = 1


def another():
    color = "blue"  # local
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)  # local before/global after

    greeting("Dave")


another()
