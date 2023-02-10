current = "1"

for i in range(5):
    direct = input()
    if direct == "up":
        if int(current) > 0:
            current = str(int(current)+1)
        elif current == "B1":
            current = "1"
        else:
            current = current[0] + str(int(current)-1)
    elif direct == "down":
        if current == "1":
            current = "B1" 
        elif int(current) > 0:
            current = str(int(current)-1)
        else:
            current = current[0] + str(int(current)+1)