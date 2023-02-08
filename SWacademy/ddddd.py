def abc(level):
    if level == 2:
        return

    abc(level + 1)
    abc(level + 1)
    dummy = 1


abc(0)