from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -6.0)
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w)/float(h), 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)

def load_model():
    with open("C:/Users/Sagol grg/Desktop/ground_control_v3-main/lowrocket.obj") as f:
        lines = f.read().splitlines()
    vertices = []
    faces = []
    for line in lines:
        if line.startswith("v "):
            vertices.append(list(map(float, line.split()[1:4])))
        elif line.startswith("f "):
            faces.append([int(x.split("/")[0])-1 for x in line.split()[1:4]])
    return vertices, faces

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1080, 720)
glutCreateWindow("Rocket")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glEnable(GL_DEPTH_TEST)
vertices, faces = load_model()
glutMainLoop()
