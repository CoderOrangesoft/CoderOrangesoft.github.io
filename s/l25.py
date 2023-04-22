# 请你编写完整代码
import opt

def tank_update():
    x = opt.BALL.x
    y = opt.BALL.y
    return move_to(x-2,y)

def move_to(tx,ty):
    angle = opt.TANK.angle_to(tx-2,ty)
    if 0 < angle <= 45:
        vs, hs = 0.9, -0.6
    elif 45 < angle <= 90:
        vs, hs = 0.6, -0.9
    elif 90 < angle <= 135:
        vs, hs = -0.6, -0.9
    elif 135 < angle <= 180:
        vs, hs = -0.9, -0.6
    elif 180 < angle <= 225:
        vs, hs = -0.9, 0.6
    elif 225 < angle <= 270:
        vs, hs = -0.6, 0.9
    elif 270 < angle <= 315:
        vs, hs = 0.6, 0.9
    elif 315 < angle <= 360:
        vs, hs = 0.9, 0.6
    return vs, hs
