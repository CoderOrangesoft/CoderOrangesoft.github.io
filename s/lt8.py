import opt
flag = 1

def control_speed(angle):
    if 0 <= angle < 45:
        return 1, -0.3
    elif 45 <= angle < 90:
        return 0.3,-1
    elif 90 <= angle < 135:
        return -0.3,-1
    elif 135 <= angle < 180:
        return -1,-0.3
    elif 180 <= angle < 225:
        return -1,0.3
    elif 225 <= angle < 270:
        return -0.3,1
    elif 270 <= angle < 315:
        return 0.3,1
    else:
        return 1,0.3

def tank_update():
    global flag
    me = opt.TANK
    ball = opt.BALL
    if flag == 1:
        me.do_fire()
        flag = 2
        return 0,0
    elif flag == 2:
        
        if me.is_point_in_range(-12,24,2):
            flag = 3
            vs,hs = 0,0
        else:
            angle = me.angle_to(-12,24)
            vs,hs =control_speed(angle)
        return vs,hs    
    if flag == 3:
        angle = me.angle_to(ball.x,ball.y)
        if -1 < angle < 1:
            me.do_fire()
            return 0,0
        else:
            return -0.3,-1

