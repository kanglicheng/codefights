def newRoadSystem(roadRegister):
    s = 0
    t = 0

    for i in range(len(roadRegister)):
        s = 0
        t = 0

        for j in range(len(roadRegister[i])):
            if roadRegister[i][j] == True:
                s += 1

            if roadRegister[j][i] == True:
                t += 1

        if s != t:
            return False

    return True
