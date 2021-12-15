import itertools
import mcpi.block as block
import mcpi.minecraft as minecraft
import time
import math

mc = minecraft.Minecraft.create()


def drange(start, stop, step): #custom function to calculate values since range() doesn't support floats
    r = start
    while r < stop:
        yield r
        r += step


R = 2
r = 1
phi = 0
phiSpeed = 0.01
points = []
TWO_PI = math.pi*2
done = False
oPoints = []
after = 314 #after how many blocks it should fill air, 314 its after half rotation because of 3.14 half circle you know...
mult = 5 #faster way of writing R = 10 r = 5, generally if you want bigger torus play with this not R and r to keep ratios same
time.sleep(2)

half = False  # set it to True if you want half torus

while not done:

    time.sleep(0.005)

    while len(oPoints) > after+1:
        oPoints.pop(0)

    if half == True:
        for x in range(len(oPoints)-after):
            for p in oPoints[x]:
                mc.setBlock(p, block.AIR)

    th = drange(0.0, TWO_PI, math.radians(1)) #the less radians the more detail, but no point goin lower because you gonna place blocks in the exact same location

    for theta in th:
        xoff = (R + r * math.cos(theta)) * math.cos(phi) * mult
        zoff = (R + r * math.cos(theta)) * math.sin(phi) * mult
        yoff = r * math.sin(theta) * mult

        points.append([math.floor(xoff), math.floor(yoff)+150, math.floor(zoff)]) #Do you see the +150? Yea thats how hight it gonna spawn. So change to your needs

    points = list(points for points, _ in itertools.groupby(points))

    phi += phiSpeed

    for p in points:
        mc.setBlock(p, block.GOLD_BLOCK)

    if phi >= TWO_PI:
        phi = 0

    oPoints.append(points)
    points = []
