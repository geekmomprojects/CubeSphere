#Functions to transform 3D coordinates
import math

def sphericalToCartesian(rho, theta, phi) :
    x = rho*math.sin(phi)*math.cos(theta)
    y = rho*math.sin(phi)*math.sin(theta)
    z = rho*math.cos(phi)
    return [x, y, z]

def cartesianToSpherical(x, y, z) :
    rho = math.sqrt(x*x + y*y + z*z)
    theta = math.atan2(y,x)
    phi = math.acos(z/rho)
    return [rho, theta, phi]

# rotate points in Cartesian coordinates by an angle theta around the x axis
def rotateCartesianPtsX(pts, theta):
    c = math.cos(theta)
    s = math.sin(theta)
    rotated = []
    for p in pts:
        rotated.append([p[0], c*p[1] - s*p[2], s*p[1] + c*p[2]])
    return rotated

def rotateCartesianPtsY(pts, theta):
    c = math.cos(theta)
    s = math.sin(theta)
    rotated = []
    for p in pts:
        rotated.append([c*p[0] +s*p[2], p[1], c*p[2] - s*p[0]])
    return rotated


#Centers values at origin in 3d and normalized values to [-1,1]
def normalize(pts):
    pmin = pts[0].copy()
    pmax = pts[0].copy()
    np = len(pmin)

    for pt in pts:
        for i in range(np):
            if pt[i] < pmin[i]:
                pmin[i] = pt[i]
            if pt[i] > pmax[i]:
                pmax[i] = pt[i]

    for i in range(np):
        mid = (pmin[i] + pmax[i])/2
        spread = (pmax[i] - pmin[i])/2
        for p in pts:
            p[i] = (p[i] - mid)/spread
    return pts











