def greatRenaming(roadRegister):
    r = roadRegister.pop()
    roadRegister.insert(0, r)

    for i in range(len(roadRegister)):
        q = roadRegister[i].pop()
        roadRegister[i].insert(0, q)

    return roadRegister
