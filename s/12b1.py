import opt
import random

#在这里输入密码
password = ""

#0为防守，1为攻击，2为随机
#这里已经调好配置了 对战大力出奇迹4:1 十分好用
if ((password[8] == "a") and (password[9] == "n")):
    print("[PASSWORD PROTECT 1A]密码验证成功!")
    TANK1 = 1
    TANK2 = 1
    TANK3 = 1
    TANK4 = 0
    TANK5 = 3

if (password[1] != "i"):
    #密码保护程序
    password = 0
    TANK1 = 0
    TANK2 = 0
    TANK3 = 0
    TANK4 = 0
    TANK5 = 0
    print("[PASSWORD PROTECT 2A]密码验证失败!")
    print("[PASSWORD PROTECT 2B]代码停止!")
else:
    print("[PASSWORD PROTECT 2A]密码验证成功!")

#不要动 不然输了我不负责
if (password):
    #密码保护程序
    r1 = random.randint(0,1)
    r2 = random.randint(0,1)
    r3 = random.randint(0,1)
    r4 = random.randint(0,1)
    r5 = random.randint(0,1)

def tank1_update():
    global password
    if (password):
        global TANK1
        if TANK1 == 0:
            return defence()
        elif TANK1 == 1:
            return attack()
        elif TANK1 == 3:
            return doorKeeper()
        else:
            if r1 == 1:
                return attack()
            else:
                return defence()


def tank2_update():
    global password
    if (password):
        global TANK2
        if (password):
            if TANK2 == 1:
                return attack()
            elif TANK2 == 0:
                return defence()
            elif TANK2 == 3:
                return doorKeeper()
            else:
                if r2 == 1:
                    return attack()
                else:
                    return defence()


def tank3_update():
    global password
    global TANK3
    if TANK3 == 1:
        if (password):
            return attack()
        else:
            print("[PASSWORD PROTECT 3A](with function)密码验证失败!")
            return 0,0
    elif TANK3 == 0:
        return defence()
    elif TANK3 == 3:
        return doorKeeper()
    else:
        if r3 == 1:
            return attack()
        else:
            return defence()


def tank4_update():
    global password
    global TANK4
    if TANK4 == 1:
        return attack()
    elif TANK4 == 0:
        return defence()
    elif TANK4 == 3:
        return doorKeeper()
    else:
        if r4 == 1:
            return attack()
        else:
            return defence()

def tank5_update():
    global password
    global TANK5
    if TANK5 == 1:
        if (password):
            return attack()
    elif TANK5 == 0:
        return defence()
    elif TANK5 == 3:
        if (password)
            return doorKeeper()
    else:
        if r5 == 1:
            return attack()
        else:
            return defence()


# 定义机器人attack( )进攻策略的方法
def attack():
    x = opt.BALL.x
    y = opt.BALL.y
    vs, hs = move_to(x-2,y)
    print(vs,hs)
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
    if opt.BALL.x < -40 and opt.BALL.x > -20:
        vs,hs = move_to(opt.BALL.x - 2,opt.BALL.y)
    elif opt.BALL.x < -25:
        vs,hs = move_to(opt.BALL.x,opt.BALL.y)
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

def doorKeeper():
    ball_x = opt.BALL.x
    ball_y = opt.BALL.y

    if 8 > ball_y > -8:
        vs, hs = move_to(ball_x, ball_y)
    elif opt.TANK.is_point_in_range(49,0,2):
        vs, hs = 0 ,0
    else:
        vs, hs = move_to(49 , 0)
    return vs, hs
  

# 定义一个move_to(tx, ty)函数，使机器人自动向目标点(tx, ty)行驶
def move_to(tx, ty):
    angle = opt.TANK.angle_to(tx, ty)
    vs, hs = 0, 0
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
