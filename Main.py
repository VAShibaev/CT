import dicom
import os, sys
import numpy
from matplotlib import pyplot, cm
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtOpenGL import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


#------------------------------------------------------

PathDicom = "/Volumes/WININSTALL/manix"
lstFilesDCM = []
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            lstFilesDCM.append(os.path.join(dirName, filename))

pixelMap = []


for file in lstFilesDCM:
    RefDs = dicom.read_file(file)
    pixelMap.append(RefDs.pixel_array)


list_of_points = []

for z in range(0, len(pixelMap) - 1, 8):
    for y in range(0, len(pixelMap[0]) - 1, 8):
        first = True
        end_point = None
        for x in range(0, len(pixelMap[0][0]) - 1, 8):
            cof = pixelMap[z][y][x]
            if cof > 1000 and cof < 1500:
                if first:
                    first = False
                    list_of_points.append((x, y, z, cof))
                else:
                    end_point = (x, y, z, cof)
            else:
                first = True
                if end_point:
                    list_of_points.append(end_point)
                end_point = None

triangles_list = []

poligons = []

# for z in range(0, len(pixelMap) - 2, 15):
#     for y in range(0, len(pixelMap[0]) - 2, 15):
#         for x in range(0, len(pixelMap[0][0]) - 2, 15):
#             verteses_list = [None, None, None, None, None, None, None, None]
#
#             cof = pixelMap[z][y][x]
#             v1 = (x, y, z, cof)
#             if v1 in list_of_points:
#                 verteses_list[0] = v1
#
#             cof = pixelMap[z][y][x + 1]
#             v2 = (x + 1, y, z, cof)
#             if v2 in list_of_points:
#                 verteses_list[1] = v2
#
#             cof = pixelMap[z][y + 1][x + 1]
#             v3 = (x + 1, y + 1, z, cof)
#             if v3 in list_of_points:
#                 verteses_list[2] = v3
#
#             cof = pixelMap[z][y + 1][x]
#             v4 = (x, y + 1, z, cof)
#             if v4 in list_of_points:
#                 verteses_list[3] = v4
#
#             cof = pixelMap[z + 1][y][x]
#             v5 = (x, y, z + 1, cof)
#             if v5 in list_of_points:
#                 verteses_list[4] = v5
#
#             cof = pixelMap[z + 1][y][x + 1]
#             v6 = (x + 1, y, z + 1, cof)
#             if v6 in list_of_points:
#                 verteses_list[5] = v6
#
#             cof = pixelMap[z + 1][y + 1][x + 1]
#             v7 = (x + 1, y + 1, z + 1, cof)
#             if v7 in list_of_points:
#                 verteses_list[6] = v7
#
#             cof = pixelMap[z + 1][y + 1][x]
#             v8 = (x, y + 1, z + 1, cof)
#             if v8 in list_of_points:
#                 verteses_list[7] = v8
#
#
#
# def define_poligone(verteses_list):
#     if verteses_list[0] == None and \
#         verteses_list[1] == None and \
#         verteses_list[2] == None and \
#         verteses_list[3] == None and \
#         verteses_list[4] == None and \
#         verteses_list[5] == None and \
#         verteses_list[6] == None and \
#         verteses_list[7] == None:
#         pass



#------------------------------------------------------

class MainWindow(QGLWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(300, 300)
        self.xRotation = 0.0;
        self.yRotation = 0.0;
        self.zRotation = 0.0;
        self.scale = 1;
        self.mousePos = None
        global pixelMap
        self.zl = len(pixelMap) // 2
        self.yl = len(pixelMap[0]) // 2
        self.xl = len(pixelMap[0][0]) // 2

    def initializeGL(self):
        self.qglClearColor(QColor(255, 255, 255))
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_FLAT)
        glDisable(GL_CULL_FACE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def resizeGL(self, p_int, p_int_1):
        glViewport(0, 0, p_int, p_int_1)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glScalef(self.scale, self.scale, self.scale)
        glRotatef(self.xRotation, 1.0, 0.0, 0.0)
        glRotatef(self.yRotation, 0.0, 1.0, 0.0)
        glRotatef(self.zRotation, 0.0, 0.0, 1.0)

        self.drawAxis()



        global list_of_points
        global color
        global triangles_list

        # for line in triangles_list:
        #     cof = math.ceil(255 / 4095 * line[0][3])
        #     color = QColor(cof, cof, cof, 255)
        #     self.qglColor(color)
        #     glBegin(GL_LINE)
        #     glVertex3f(1.0 / self.xl * (line[0][0] - self.xl),
        #            1.0 / self.yl * (line[0][1] - self.yl),
        #            1.0 / self.zl * (line[0][2] - self.zl))
        #     glVertex3f(1.0 / self.xl * (line[1][0] - self.xl),
        #            1.0 / self.yl * (line[1][1] - self.yl),
        #            1.0 / self.zl * (line[1][2] - self.zl))
        #     glEnd()
        #color = QColor(cof, cof, cof, 255)
        for point in  list_of_points:
            cof = math.ceil(255 / 4095 * point[3])
            color = QColor(cof, cof, cof, 255)
            self.qglColor(color)


            glBegin(GL_POINTS)
            glVertex3f(1.0 / self.xl * (point[0] - self.xl),
                       1.0 / self.yl * (point[1] - self.yl),
                       1.0 / self.zl * (point[2] - self.zl))
            glEnd()

    def mousePressEvent(self, event):
        self.mousePos = event.pos()

    def mouseMoveEvent(self, event):
        self.xRotation += 180/self.scale * (event.y() - self.mousePos.y())/self.height()
        self.zRotation += 180/self.scale * (event.x() - self.mousePos.x())/self.width()
        self.mousePos = event.pos()
        self.updateGL()

    def mouseReleaseEvent(self, event):
        pass

    def wheelEvent(self, event):
        if ((event.delta())>0):
            self.scale *=1.1
        else:
            if ((event.delta())<0):
                self.scale /= 1.1
        self.updateGL()

    def drawAxis(self):
        glLineWidth(3.0)
        glColor4f(1.0, 0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        glVertex3f(1.0, 0.0, 0.0)
        glVertex3f(-1.0, 0.0, 0.0)
        glEnd()

        halfGreen = QColor(0, 128, 0, 255)
        self.qglColor(halfGreen)
        glBegin(GL_LINES)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, -1.0, 0.0)
        glEnd()
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, -1.0)
        glEnd()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Qt OpenGL")
    window.setGeometry(100, 100, 500, 500)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__": main()