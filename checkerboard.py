

def newLocations(location, corner):
    top, left = location
    ct, cl = corner
    return [(top, left), (ct, left), (top, cl)]

def newCorners(location, corner):
    top, left = location
    ct, cl = corner
    dt, dl = ct - top, cl - left
    ddt, ddl = dt / abs(dt), dl / abs(dl)
    dt, dl = abs(dt) / 2 * ddt, abs(dl) / 2 * ddl
    ct1, cl1 = top + dt, left + dl
    ct2, cl2 = ct1 + ddt, cl1
    ct3, cl3 = ct1, cl1 + ddl

    newCorners = [(ct1, cl1), (ct2, cl2), (ct3, cl3)]
    return newCorners

def cover(board, location, corner, lab = 1, side = None):
    if side is None: side = len(board)
    cords = newCorners(location, corner);
    for t, l in cords:
        board[t][l] = lab

    lab += 1
    top, left = location
    ctop, cleft = corner
    if(abs(top - ctop) == 1 and abs(left - cleft) == 1):
        return lab
    else:
        pass

if __name__ == '__main__':
    print '*' * 10
    print newCorners((0,0), (7,7))
    print newLocations((0,0), (7,7))
    print newCorners((0,7), (3,4))
    print newLocations((0,7), (3,4))
    print newCorners((7,0), (4,3))
    print newCorners((4,4), (7,7))
    print newCorners((0,0), (1,1))
    print newCorners((7,0), (6,1))
