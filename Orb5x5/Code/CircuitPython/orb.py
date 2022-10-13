from coordinates import *
from collections import OrderedDict
import neopixel

#Orb and matrix class
class Matrix:
    X=1  # To define axes
    Y=2
    Z=3
    def __init__(self, startpt, rowaxis, colaxis, firstindex, width, alternating=True):
        self.startpt = startpt
        rowdir = rowaxis//abs(rowaxis)
        rowval = abs(rowaxis)
        self.rowinc = [0, 0, 0]
        self.rowinc[rowval-1] = rowdir
        coldir = colaxis//abs(colaxis)
        colval = abs(colaxis)
        self.colinc = [0, 0, 0]
        self.colinc[colval-1] = coldir
        self.alt = alternating
        self.width = width
        self.first = firstindex
        self.last = firstindex + width*width
        #print(self.rowinc, self.colinc)

    @classmethod
    def axis_index(cls, axis):
        mag = abs(axis)
        if mag >= cls.X and mag <= cls.Z:
            return mag - 1
        else:
            return None

    @classmethod
    def axis_dir(cls, axis):
        mag = abs(axis)
        if mag >= cls.X and mag <= cls.Z:
            return axis//abs(axis)
        else:
            return None


class Orb:
    def __init__(self, width, matrix_list, matrix_names, pixels):
        self.width = width
        self.cart = []
        self.spher = []
        self.pixels = pixels
        self.matrix_dict = OrderedDict()
        # Using the fact that Python 3.7 and up means dictionaries are ordered
        for i in range(len(matrix_names)):
            self.matrix_dict[matrix_names[i]] = matrix_list[i]
        cube_coords = self.make_cube(matrix_list)
        # now that we have the normalized coordinates of the pixels
        # on the matrices which comprise the cube, get the
        # coordinates of the points on the surface of the orb
        radius = math.sqrt(3)*1.15
        new_cart = []
        for c in cube_coords:
            s = cartesianToSpherical(*c)
            s[0] = radius
            self.spher.append(s[1:3])  # only save angular coords. R doesnt matter
            self.cart.append(sphericalToCartesian(*s))
        #print(self.spher)
        normalize(self.cart)
        #print(self.cart)



    def opp(self,x):
        return self.width - x - 1

    #Returns coordinates for a width x width matrix with the specified
    #orientation in right-handed [X,Y,Z] space. Assumes pixels laid out
    #in rows, then rows stacked in columns. rowinc, colinc is how much
    #each cartesian coordinate changes in each step in the row and column
    #directions respectively. For a regular square grid, values will be -1, 0 or 1
    #e.g. for a matrix in the XZ plane, with the first pixel at [width, 0, 0],
    #and alternating rows directed along the x-axis, you would specify:
    # start = [width,0,0], rowinc = [-1,0,0], colinc=[0,0,1]. alt is true
    # if row directions alternate, false if all rows run in the same direction
    def matrix_coords(self, startpt, rowinc, colinc, alt=True):
        coords = []
        nc = len(startpt)
        for col in range(self.width):
            firstpt = [startpt[k] + col*colinc[k] for k in range(nc)]
            #print(firstpt)
            for row in range(self.width):
                pt = [firstpt[k] + row*rowinc[k] for k in range(nc)]
                if alt and col % 2 == 1:
                    for k in range(nc):
                        if rowinc[k]:
                            pt[k] = self.opp(pt[k])
                coords.append(pt)
        return coords

    def make_cube(self, matrix_list):
        coords = []
        for matrix in matrix_list:
            coords = coords + self.matrix_coords(matrix.startpt, matrix.rowinc, matrix.colinc, matrix.alt)
            #print("lenght of coords = ", len(coords))
        return normalize(coords)

    def fill_matrix(self, mat, color, do_show=True):
        matrix = None
        if isinstance(mat, str):
            matrix = self.matrix_dict(mat)
        elif isinstance(mat, int):
            key = list(self.matrix_dict)[mat]
            matrix = self.matrix_dict[key]

        if matrix is not None:
            self.pixels[matrix.first:matrix.last] = [color]*(self.width*self.width)
            if do_show:
                self.show()

    def matrix_name(self, num):
        return list(self.matrix_dict)[num]

    def fill_above(self, axis, cutoff, color):
        axis_val = Matrix.axis_index(axis)
        for i in range(self.pixels.n):
            self.pixels[i] = color if self.cart[i][axis_val] > cutoff else (0,0,0)

    def show(self):
        self.pixels.show()