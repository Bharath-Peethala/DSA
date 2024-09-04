# neetcode sol - https://www.youtube.com/watch?v=wpglWC6mnLg

def robot(commands,obs):
    x,y = 0,0
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    obs = { tuple(o) for o in obs }
    d = 0
    res = 0
    for c in commands:
        if c == -1:
            d = (d+1) % 4
        elif c == -2:
            d = (d-1) % 4
        else:
            dx,dy = directions[d]
            for _ in range(c):
                if (x+dx, y+dy) in obs:
                    break
                x,y = x+dx,y+dy
            res = max(res, x**2 + y**2)
    return res

print(robot([4,-1,4,-2,4],[[2,4]]))


