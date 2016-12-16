# -*- coding: utf-8 -*-
from satellite import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

class thaicom(satellite):

    #Class Variable
    solarFile = "texture/solarpanelmap.jpg"
    bodyFile = "texture/spaceshipmap1.jpg"

    #Constructor
    def __init__(self, scale):
        super(thaicom, self).__init__()
        
        self.scaleDraw = scale
        
        #texture variable
        self.solarSurf = pygame.image.load(thaicom.solarFile)
        self.solarImage = pygame.image.tostring(self.solarSurf, "RGB", 1) # Flip image for OpenGL. See pygame doc.
        self.bodySurf = pygame.image.load(thaicom.bodyFile)
        self.bodyImage = pygame.image.tostring(self.bodySurf, "RGB", 1) # Flip image for OpenGL. See pygame doc.


        # Defining texture
        self.allTexture = glGenTextures(2)

        #Solar texture
        glBindTexture(GL_TEXTURE_2D, self.allTexture[0])
        glTexImage2D(GL_TEXTURE_2D,
                               0,   # level
                               3,   # components (3 for RGB)
                               self.solarSurf.get_width(),  # width
                               self.solarSurf.get_height(),  # height
                               0,   #border
                               GL_RGB, # format
                               GL_UNSIGNED_BYTE,  # type
                               self.solarImage)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        
        #Body texture
        glBindTexture(GL_TEXTURE_2D, self.allTexture[1])
        glTexImage2D(GL_TEXTURE_2D,
                               0,   # level
                               3,   # components (3 for RGB)
                               self.bodySurf.get_width(),  # width
                               self.bodySurf.get_height(),  # height
                               0,   #border
                               GL_RGB, # format
                               GL_UNSIGNED_BYTE,  # type
                               self.bodyImage)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # GL_LINEAR
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        
        self.corners = [[0, 0, 0], [-6, 0, 0], [-6, 0, 7], [-5, 0, 7], [-5, 0, 8], [-1, 0, 8], [-1, 0, 7], [0, 0, 7], #Left Point
                        [0, 5, 0], [-6, 5, 0], [-6, 5, 7], [-5, 5, 7], [-5, 5, 8], [-1, 5, 8], [-1, 5, 7], [0, 5, 7], #Right Point
                        ]
        self.draw_position = [[0, 0, 0], [-6, 0, 0], [-6, 0, 7], [-5, 0, 7], [-5, 0, 8], [-1, 0, 8], [-1, 0, 7], [0, 0, 7], #Left Point
                        [0, 5, 0], [-6, 5, 0], [-6, 5, 7], [-5, 5, 7], [-5, 5, 8], [-1, 5, 8], [-1, 5, 7], [0, 5, 7], #Right Point
                        ]
        self.planes = [[0, 1, 2, 7], [4, 5, 6, 3], #Left Plane
                       [8, 9, 10, 15], [12, 13, 14, 11], #Right Plane
                       ]#, [1, 2, 7, 6], [2, 3, 4, 7], [0, 3, 4, 5]]
        self.lines = [[0, 1], [1, 2], [2, 3], [3, 4], [4,5], [5, 6], [6, 7], [7, 0], #Left Line
                      [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 8], #Right Line
                      [0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15] #Connect Left and Right
                      ]
                      
        self.rotate_angle = 0
        self.rotate_angle2 = 0
        
        self.quad = gluNewQuadric()
        gluQuadricDrawStyle(self.quad, GLU_FILL) #GLU_FILL , GLU_LINE , GLU_SILHOUETTE , and GLU_POINT
        gluQuadricNormals(self.quad, GLU_SMOOTH) #GLU_NONE , GLU_FLAT , and GLU_SMOOTH
        gluQuadricTexture(self.quad, GL_TRUE)
        
        
    def draw(self):
        for i in range(len(self.corners)):
            self.draw_position[i][0] = (self.corners[i][0]) + self.getPosition()[0]
            self.draw_position[i][1] = (self.corners[i][1]) + self.getPosition()[1]
            self.draw_position[i][2] = (self.corners[i][2]) + self.getPosition()[2]
        
        glPushMatrix()
        glBegin(GL_QUADS)
        #glEnable(GL_TEXTURE_2D)
        #glBindTexture(GL_TEXTURE_2D, self.allTexture[1])
        for plane_pair in self.planes:
            #glColor3fv(planes_color[0])
            #color_selector += 1
            glVertex3f(self.draw_position[plane_pair[0]][0],self.draw_position[plane_pair[0]][1],self.draw_position[plane_pair[0]][2])
            glVertex3f(self.draw_position[plane_pair[1]][0],self.draw_position[plane_pair[1]][1],self.draw_position[plane_pair[1]][2])
            glVertex3f(self.draw_position[plane_pair[2]][0],self.draw_position[plane_pair[2]][1],self.draw_position[plane_pair[2]][2])
            glVertex3f(self.draw_position[plane_pair[3]][0],self.draw_position[plane_pair[3]][1],self.draw_position[plane_pair[3]][2])
        #glDisable(GL_TEXTURE_2D)
        glEnd()
        
        #Draw Lines
        glBegin(GL_LINES)
        for corner_pair in self.lines:
            glVertex3f(self.draw_position[corner_pair[0]][0],self.draw_position[corner_pair[0]][1],self.draw_position[corner_pair[0]][2])
            glVertex3f(self.draw_position[corner_pair[1]][0],self.draw_position[corner_pair[1]][1],self.draw_position[corner_pair[1]][2])
        glEnd()

        #Restore Original Matrix
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(self.draw_position[7][0], self.draw_position[7][1], self.draw_position[7][2])
        glRotatef(self.rotate_angle, 0, 1, 0)
        glRotatef(33, -1, 0, 0)
        gluCylinder( self.quad , 0.1 , 0.1 , 4.6 , 36 , 36 )
        glTranslatef(0, 0, 4.6)
        glRotatef(90, 0, 1, 0)
        #glColor(255,255,255)
        gluDisk( self.quad , 0 , 2.5 , 36, 36 )
        glPopMatrix()

        glPushMatrix()
        glTranslatef(self.draw_position[15][0], self.draw_position[15][1], self.draw_position[15][2])
        glRotatef(self.rotate_angle-5, 0, 1, 0)
        glRotatef(33, 1, 0, 0)
        gluCylinder( self.quad , 0.1 , 0.1 , 4.6 , 36 , 36 )
        glTranslatef(0, 0, 4.6)
        glRotatef(90, 0, 1, 0)
        #glColor(255,255,255)
        gluDisk( self.quad , 0 , 2.5 , 36, 36 )
        glPopMatrix()


        
        glPushMatrix()
        glTranslatef((self.draw_position[7][0] + self.draw_position[2][0])/2, self.draw_position[0][1], (self.draw_position[0][2] + self.draw_position[5][2])/2)
        glRotatef(self.rotate_angle2, 1, 0, 0)
        gluCylinder( self.quad , 0.1 , 0.1 , 1 , 36 , 36 )
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.allTexture[0])
        glTranslatef(0, 0, 3.5)
        glRotatef(90, 1, 0, 0)
        glRotatef(45, 0, 0, 1)
        #glRotatef(rotate_angle2, -1, 0, 0)
        gluDisk(self.quad, 0, 3.5, 4, 4  )
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef((self.draw_position[10][0] + self.draw_position[15][0])/2, self.draw_position[8][1], (self.draw_position[8][2] + self.draw_position[13][2])/2)
        glRotatef(self.rotate_angle2, -1, 0, 0)
        gluCylinder( self.quad , 0.1 , 0.1 , 1 , 36 , 36 )
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.allTexture[0])
        glTranslatef(0, 0, 3.5)
        glRotatef(90, 1, 0, 0)
        glRotatef(45, 0, 0, 1)
        #glRotatef(rotate_angle2, -1, 0, 0)
        gluDisk(self.quad, 0, 3.5, 4, 4  )
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()
    
    
    
    
    
    
    
        