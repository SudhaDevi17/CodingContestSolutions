queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
tking = tuple(king)
queenset = set(map(tuple, queens))
ans = []
def search(x , y ):
    print("searching ", x ,y)
    for dx in range(-1 , 2 ):
        for dy in range(-1 , 2 ):
            if dx or dy:
                cx = x +  dx
                cy = y+ dy
                print("x: dx : cx " , x , dx , cx , "   y: dy : cy "  , y, dy, cy )
                while 0 <= cx < 8 > cy >= 0:
                    node = cx, cy
                    print("WIll consider " , node)
                    if node in queenset:
                        print(" this node is in queen set, "  , node)
                        break
                    if node == tking:
                        return True
                    cx += dx
                    cy += dy
for Q in queens:
    if search(*Q):
        ans.append(Q)

print("Violent queen sits at " , ans)