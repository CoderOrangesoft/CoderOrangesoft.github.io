# 请你编写完整代码
import opt

def tank_update():
    global state
    if opt.TANK.is_point_in_range(40,0,2):
        if (0 <= opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <  40) or (320 <= opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <  360):
            return 0.6,0
        else:
            return 0.1,-0.5
    else:
            if (0 <= opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <  40) or (320 <= opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <  360):
                return 0.6,0
            angle = opt.TANK.angle_to(40,0)
            if 0 < angle <= 45:
                vs, hs = 1, -0.3
            elif 45 < angle <= 90:
                vs, hs = 0.3, -1
            elif 90 < angle <= 135:
                vs, hs = -0.3, -1
            elif 135 < angle <= 180:
                vs, hs = -1, -0.3
            elif 180 < angle <= 225:
                vs, hs = -1, 0.3
            elif 225 < angle <= 270:
                vs, hs = -0.6, 0.9
            elif 270 < angle <= 315:
                vs, hs = 0.6, 0.9
            elif 315 < angle <= 360:
                vs, hs = 0.9, 0.6
            return vs,hs
