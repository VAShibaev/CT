STEPX = 1
STEPY = 1
STEPZ = 1

# Делаем все относительно точки V1 !!!!

def e1(vertex):
    return (vertex[0] + STEPX / 2, vertex[1], vertex[2], vertex[3])

def e2(vertex):
    return (vertex[0] + STEPX, vertex[1] + STEPY / 2, vertex[2], vertex[3])

def e3(vertex):
    return (vertex[0] + STEPX / 2, vertex[1] + STEPY, vertex[2], vertex[3])

def e4(vertex):
    return (vertex[0], vertex[1] + STEPY / 2, vertex[2], vertex[3])

def e5(vertex):
    return (vertex[0] + STEPX / 2, vertex[1], vertex[2] + STEPZ, vertex[3])

def e6(vertex):
    return (vertex[0] + STEPX, vertex[1] + STEPY / 2, vertex[2] + STEPZ, vertex[3])

def e7(vertex):
    return (vertex[0] + STEPX / 2, vertex[1] + STEPY, vertex[2] + STEPZ, vertex[3])

def e8(vertex):
    return (vertex[0], vertex[1] + STEPY / 2, vertex[2] + STEPZ, vertex[3])

def e9(vertex):
    return (vertex[0], vertex[1], vertex[2] + STEPZ / 2, vertex[3])

def e10(vertex):
    return (vertex[0] + STEPX, vertex[1], vertex[2] + STEPZ / 2, vertex[3])

def e11(vertex):
    return (vertex[0], vertex[1] + STEPY, vertex[2] + STEPZ / 2, vertex[3])

def e12(vertex):
    return (vertex[0] + STEPX, vertex[1] + STEPY, vertex[2] + STEPZ / 2, vertex[3])





def isosurface(vertex_array):

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return

    result = variant1(vertex_array)
    if result:
        return result

    result = variant2(vertex_array)
    if result:
        return result

# vertex = (x, y, z, cof)

#--------------------------------------------------------------------------------
def variant1(vertex_array):
    if vertex_array[0] != None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e4(vertex_array[0]),
            e1(vertex_array[0]),
            e9(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] != None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e2(vertex_array[0]),
            e10(vertex_array[0]),
            e1(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] != None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e3(vertex_array[0]),
            e12(vertex_array[0]),
            e2(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] != None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e11(vertex_array[0]),
            e3(vertex_array[0]),
            e4(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] != None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e8(vertex_array[0]),
            e9(vertex_array[0]),
            e5(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] != None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e6(vertex_array[0]),
            e5(vertex_array[0]),
            e10(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] != None and \
        vertex_array[7] == None:
        return [(
            e7(vertex_array[0]),
            e6(vertex_array[0]),
            e12(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] != None:
        return [(
            e11(vertex_array[0]),
            e8(vertex_array[0]),
            e7(vertex_array[0])
        )]


#--------------------------------------------------------------------------------

def variant2(vertex_array):
    if vertex_array[0] != None and \
        vertex_array[1] != None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e4(vertex_array[0]),
            e2(vertex_array[0]),
            e9(vertex_array[0])
            ),
            (
            e2(vertex_array[0]),
            e10(vertex_array[0]),
            e9(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] != None and \
        vertex_array[2] != None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e1(vertex_array[0]),
            e3(vertex_array[0]),
            e10(vertex_array[0])
            ),
            (
            e10(vertex_array[0]),
            e3(vertex_array[0]),
            e12(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] != None and \
        vertex_array[3] != None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e4(vertex_array[0]),
            e11(vertex_array[0]),
            e12(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e2(vertex_array[0]),
            e4(vertex_array[0])
        )]


    if vertex_array[0] != None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] != None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e11(vertex_array[0]),
            e3(vertex_array[0]),
            e9(vertex_array[0])
            ),
            (
            e9(vertex_array[0]),
            e3(vertex_array[0]),
            e1(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] != None and \
        vertex_array[5] != None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e8(vertex_array[0]),
            e9(vertex_array[0]),
            e10(vertex_array[0])
            ),
            (
            e6(vertex_array[0]),
            e8(vertex_array[0]),
            e10(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] != None and \
        vertex_array[6] != None and \
        vertex_array[7] == None:
        return [(
            e7(vertex_array[0]),
            e5(vertex_array[0]),
            e12(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e5(vertex_array[0]),
            e10(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] != None and \
        vertex_array[7] != None:
        return [(
            e11(vertex_array[0]),
            e8(vertex_array[0]),
            e12(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e8(vertex_array[0]),
            e6(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] != None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] != None:
        return [(
            e11(vertex_array[0]),
            e9(vertex_array[0]),
            e5(vertex_array[0])
            ),
            (
            e7(vertex_array[0]),
            e11(vertex_array[0]),
            e5(vertex_array[0])
        )]

    if vertex_array[0] != None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] != None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e8(vertex_array[0]),
            e4(vertex_array[0]),
            e1(vertex_array[0])
            ),
            (
            e8(vertex_array[0]),
            e1(vertex_array[0]),
            e5(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] != None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] != None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e2(vertex_array[0]),
            e6(vertex_array[0]),
            e5(vertex_array[0])
            ),
            (
            e5(vertex_array[0]),
            e1(vertex_array[0]),
            e2(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] != None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] != None and \
        vertex_array[7] == None:
        return [(
            e7(vertex_array[0]),
            e3(vertex_array[0]),
            e6(vertex_array[0])
            ),
            (
            e3(vertex_array[0]),
            e2(vertex_array[0]),
            e6(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] != None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] != None:
        return [(
            e7(vertex_array[0]),
            e3(vertex_array[0]),
            e8(vertex_array[0])
            ),
            (
            e8(vertex_array[0]),
            e3(vertex_array[0]),
            e4(vertex_array[0])
        )]



#--------------------------------------------------------------------------------

def variant3(vertex_array):
    if vertex_array[0] != None and \
        vertex_array[1] == None and \
        vertex_array[2] != None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e4(vertex_array[0]),
            e1(vertex_array[0]),
            e9(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e2(vertex_array[0]),
            e3(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] != None and \
        vertex_array[2] == None and \
        vertex_array[3] != None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e2(vertex_array[0]),
            e10(vertex_array[0]),
            e1(vertex_array[0])
            ),
            (
            e11(vertex_array[0]),
            e3(vertex_array[0]),
            e4(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] != None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] != None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e2(vertex_array[0]),
            e3(vertex_array[0]),
            e12(vertex_array[0])
            ),
            (
            e6(vertex_array[0]),
            e5(vertex_array[0]),
            e10(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] != None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] != None and \
        vertex_array[7] == None:
        return [(
            e1(vertex_array[0]),
            e2(vertex_array[0]),
            e10(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e7(vertex_array[0]),
            e6(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] != None and \
        vertex_array[6] == None and \
        vertex_array[7] != None:
        return [(
            e7(vertex_array[0]),
            e11(vertex_array[0]),
            e8(vertex_array[0])
            ),
            (
            e6(vertex_array[0]),
            e5(vertex_array[0]),
            e10(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] != None and \
        vertex_array[5] == None and \
        vertex_array[6] != None and \
        vertex_array[7] == None:
        return [(
            e8(vertex_array[0]),
            e9(vertex_array[0]),
            e5(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e7(vertex_array[0]),
            e6(vertex_array[0])
        )]


    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] != None and \
        vertex_array[4] != None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e3(vertex_array[0]),
            e4(vertex_array[0]),
            e11(vertex_array[0])
            ),
            (
            e8(vertex_array[0]),
            e9(vertex_array[0]),
            e5(vertex_array[0])
        )]

    if vertex_array[0] != None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] != None:
        return [(
            e7(vertex_array[0]),
            e11(vertex_array[0]),
            e8(vertex_array[0])
            ),
            (
            e4(vertex_array[0]),
            e1(vertex_array[0]),
            e9(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] != None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] != None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e1(vertex_array[0]),
            e2(vertex_array[0]),
            e10(vertex_array[0])
            ),
            (
            e8(vertex_array[0]),
            e8(vertex_array[0]),
            e9(vertex_array[0])
        )]

    if vertex_array[0] != None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] != None and \
        vertex_array[6] == None and \
        vertex_array[7] == None:
        return [(
            e4(vertex_array[0]),
            e1(vertex_array[0]),
            e9(vertex_array[0])
            ),
            (
            e6(vertex_array[0]),
            e5(vertex_array[0]),
            e10(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] == None and \
        vertex_array[3] != None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] != None and \
        vertex_array[7] == None:
        return [(
            e3(vertex_array[0]),
            e4(vertex_array[0]),
            e11(vertex_array[0])
            ),
            (
            e12(vertex_array[0]),
            e7(vertex_array[0]),
            e6(vertex_array[0])
        )]

    if vertex_array[0] == None and \
        vertex_array[1] == None and \
        vertex_array[2] != None and \
        vertex_array[3] == None and \
        vertex_array[4] == None and \
        vertex_array[5] == None and \
        vertex_array[6] == None and \
        vertex_array[7] != None:
        return [(
            e7(vertex_array[0]),
            e11(vertex_array[0]),
            e8(vertex_array[0])
            ),
            (
            e2(vertex_array[0]),
            e3(vertex_array[0]),
            e12(vertex_array[0])
        )]

#--------------------------------------------------------------------------------