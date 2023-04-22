import opt


# 定义一个move_to（tx,ty）函数，使机器人自动向目标点(tx,ty)行驶
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




def tank1_update():
    # 在指定区域时停下来
    if opt.TANK.is_point_in_range(40,0,4):
        vs,hs = 0,0
        return vs,hs
    # 如果不在指定区域，则移动至指定区域
    else:
        angle = opt.TANK.angle_to(40, 0)
        if 0 <= angle < 90:
            vs, hs = 1, -0.3
        elif 90 <= angle < 180:
            vs, hs = -1, -0.3
        elif 180 <= angle < 270:
            vs, hs = -1, 0.3
        elif 270 <= angle < 360:
            vs, hs = 1, 0.3
        return vs, hs


def tank2_update():
    # 在指定区域时停下来
    if opt.TANK.is_point_in_range(40,0,4):
        vs,hs = 0,0
        return vs,hs
    # 如果不在指定区域，则移动至指定区域
    else:
        angle = opt.TANK.angle_to(40, 0)
        if 0 <= angle < 90:
            vs, hs = 1, -0.3
        elif 90 <= angle < 180:
            vs, hs = -1, -0.3
        elif 180 <= angle < 270:
            vs, hs = -1, 0.3
        elif 270 <= angle < 360:
            vs, hs = 1, 0.3
        return vs, hs
