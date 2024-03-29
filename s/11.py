import opt
import random

#0为防守，1为攻击，2为随机
TANK1 = 1
TANK2 = 0
TANK3 = 0
TANK4 = 2
TANK5 = 0

# 在虚拟机器人足球中，每秒80帧，每帧都会自动调用tank_update()函数控制机器人在这一帧的行为，该函数的功能需由你自己定义。
# 该示例程序帮你定义好了基本的进攻方法attack()和基本的防守方法defence()。
# 请你修改5个机器人的update()函数，分别调用attack()进攻方法defence()防守方法。

# 控制你的 1 号机器人
def tank1_update():
    global TANK1
    # 在下一行输入return attack( )，机器人将采取进攻策略
    # 在下一行输入return defence( )，机器人将采取防守策略
    if TANK1 == 0:
        return attack()
    elif TANK1 == 1:
        return defence()
    else:
        if random.randint(0,1) == 1:
            return attack()
        else:
            return defence()



# 控制你的 2 号机器人
def tank2_update():
    global TANK2
    # 在下一行输入return attack( )，机器人将采取进攻策略
    # 在下一行输入return defence( )，机器人将采取防守策略
    if TANK2 == 0:
        return attack()
    elif TANK2 == 1:
        return defence()
    else:
        if random.randint(0,1) == 1:
            return attack()
        else:
            return defence()


# 控制你的 3 号机器人
def tank3_update():
    global TANK3
    # 在下一行输入return attack( )，机器人将采取进攻策略
    # 在下一行输入return defence( )，机器人将采取防守策略
    if TANK3 == 0:
        return attack()
    elif TANK3 == 1:
        return defence()
    else:
        if random.randint(0,1) == 1:
            return attack()
        else:
            return defence()


# 控制你的 4 号机器人
def tank4_update():
    global TANK4
    # 在下一行输入return attack( )，机器人将采取进攻策略
    # 在下一行输入return defence( )，机器人将采取防守策略
    if TANK4 == 0:
        return attack()
    elif TANK4 == 1:
        return defence()
    else:
        if random.randint(0,1) == 1:
            return attack()
        else:
            return defence()


# 控制你的 5 号机器人
def tank5_update():
    global TANK5
    # 在下一行输入return attack( )，机器人将采取进攻策略
    # 在下一行输入return defence( )，机器人将采取防守策略
    if TANK5 == 0:
        return attack()
    elif TANK5 == 1:
        return defence()
    else:
        if random.randint(0,1) == 1:
            return attack()
        else:
            return defence()


# 定义机器人attack( )进攻策略的方法
def attack():
    vs, hs = 0, 0
    # 控制机器人移动的唯一方法是设置速度vs的值[-1,+1]和转动方向hs的值[-1,+1]
    # 首先，获取足球相对于机器人的角度，并储存在变量angle中
    angle = opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)

    # 如果足球在机器人0-90度范围内，设置机器人速度vs为前进0.8，转动方向hs为左转-0.3
    if angle > 0 and angle <= 90:
        vs, hs = 0.8, -0.3

    # 如果足球在机器人90-180度范围内，设置机器人速度vs为后退-0.8，转动方向hs为左转-0.3
    elif angle > 90 and angle <= 180:
        vs, hs = -0.8, -0.3

    # 如果足球在机器人180-270度范围内，设置机器人速度vs为后退-0.8，转动方向hs为右转0.3
    elif angle > 180 and angle <= 270:
        vs, hs = -0.8, 0.3

    # 如果足球在机器人270-360度范围内，设置机器人速度vs为前进0.8，转动方向hs为右转0.3
    elif angle > 270 and angle <= 360:
        vs, hs = 0.8, 0.3
    angle_ball = opt.TANK.angle_to(opt.BALL.x,opt.BALL.y)
    if opt.TANK.cool_remain == 0:
        if angle_ball > 0 and angle_ball < 4:
            opt.TANK.do_fire()
        if angle_ball > 356 and angle_ball < 360:
            opt.TANK.do_fire()
    # 当attack()被tank_update()调用时，每一帧都会执行以上策略，并返回vs,hs值
    return vs, hs


# 定义机器人defence( )防守策略的方法
def defence():
    vs, hs = 0, 0
    # 如果足球的x坐标小于-40，进入防守范围，机器人追击足球
    if opt.BALL.x < -40:
        angle = opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)
        if angle > 0 and angle <= 90:
            vs, hs = 0.8, -0.3
        elif angle > 90 and angle <= 180:
            vs, hs = -0.8, -0.3
        elif angle > 180 and angle <= 270:
            vs, hs = -0.8, 0.3
        elif angle > 270 and angle <= 360:
            vs, hs = 0.8, 0.3

    # 否则，超出防守范围，机器人驶向并停在（-48,0）坐标附近
    else:
        if opt.TANK.is_point_in_range(-44, 0, 2):
            vs, hs = 0,0
        else:
            angle = opt.TANK.angle_to(-44, 0)
            if angle > 0 and angle <= 90:
                vs, hs = 0.8, -0.3
            elif angle > 90 and angle <= 180:
                vs, hs = -0.8, -0.3
            elif angle > 180 and angle <= 270:
                vs, hs = -0.8, 0.3
            elif angle > 270 and angle <= 360:
                vs, hs = 0.8, 0.3
    angle_ball = opt.TANK.angle_to(opt.BALL.x,opt.BALL.y)
    if opt.TANK.cool_remain == 0:
        if angle_ball > 0 and angle_ball < 4:
            opt.TANK.do_fire()
        if angle_ball > 356 and angle_ball < 360:
            opt.TANK.do_fire()

    # 当defence()被tank_update()调用时，每一帧都会执行以上策略，并返回vs,hs值
    return vs, hs
