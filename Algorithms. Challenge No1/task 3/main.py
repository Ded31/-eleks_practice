import math


def get_degrees(radians):
    degrees = int(radians * 180 / math.pi)
    return degrees
    
    
def angle(x, y):
    radians = math.atan2(y, x)
    ang = get_degrees(radians)
    return ang


def bigger_angle(AO_angle, BO_angle):
    if AO_angle > BO_angle:
        return 'AO'
    elif AO_angle == BO_angle:
        return 'Equal'
    else:
        return 'BO'


x1 = int(input('Input x1: '))
y1 = int(input('Input y1: '))
x2 = int(input('Input x2: '))
y2 = int(input('Input y2: '))

AO_angle = angle(x1, y1)
BO_angle = angle(x2, y2)

print(f'{bigger_angle(AO_angle, BO_angle)} angle is bigger')
