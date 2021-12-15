import itertools
import mcpi.block as block
import mcpi.minecraft as minecraft
import time
import math

mc = minecraft.Minecraft.create()


def drange(start, stop, step):
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
after = 314
mult = 5
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

    th = drange(0.0, TWO_PI, math.radians(1))

    for theta in th:
        xoff = (R + r * math.cos(theta)) * math.cos(phi) * mult
        zoff = (R + r * math.cos(theta)) * math.sin(phi) * mult
        yoff = r * math.sin(theta) * mult

        points.append([math.floor(xoff), math.floor(yoff)+150, math.floor(zoff)])

    points = list(points for points, _ in itertools.groupby(points))

    phi += phiSpeed

    for p in points:
        mc.setBlock(p, block.GOLD_BLOCK)

    if phi >= TWO_PI:
        phi = 0

    oPoints.append(points)
    points = []
