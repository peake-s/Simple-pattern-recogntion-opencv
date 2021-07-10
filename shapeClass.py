#-----------------------------------------------------------------------
# File : ShapeClass.py
#
# Programmers: Samuel Peake and David Wells
#
# Program #: Final Project
#
# Due Date: 05/05
#
# Course: EGRE 347, Spring 2021
#
# Pledge: I have neither given nor received unauthorized aid on this program.
#
# Description: This file contains the definitions for a class which will analyze an image to determine the order of colored shape
#               and then see if it matches an approved pattern. If the pattern is approved, it will return a 1 to the main function, otherwise a 0.
#
#-----------------------------------------------------------------------
import cv2
import numpy as np

class shapeClass:

    #Initilizer
    def __init__ (self):
        self.coordCorn = []
        self.shape = ""
        self.pattern = ""
        self.pic=0
        self.color = ""
        self.validPatterns = ["circlebluesquaregreentrianglered", "trianglegreensquareredcirclered", "hexagonblueoctagonblueheptagonblue", "octagonredtrianglegreenoctagonblue", "circlegreensquareblueoctagonblueheptagonredtriangleredsquaregreen", "circlebluehexagonredheptagongreenhexagonred"]

#  def load_shape(self, image)
#
#  Summary of the load_shape Function:
#
#     The load_shape function reads the image specified by the user and stores it in self.pic. If the image
#       was successfully loaded, then true will be returned, otherwise false will be returned
#
#  Parameters: self and an image
#
#  Return Value: bool returning true if successful, false otherwise
    def load_shape(self,image):
        self.pic = cv2.imread(image)
        if self.pic is None:
            return False
        #self.pic = cv2.imread(image)
        return True


#  def determineColor(self, x, y)
#
#  Summary of the determineColor Function:
#
#     The determineColor function is passed the midpoints of a shape from the DetermineShape function. Then the pixel at that
#       coordinate is selected and its BGR values are split up. The largest RBG value is found and then put through an else/if
#       statement to set the self.color correctly.
#
#  Parameters: self, x and y coordinates of midpoint of given shape
#
#  Return Value: returns a 0
    def determineColor(self,y,x):
        #selecting the midpoint pixel of the shape
        color = self.pic[x,y]

        #Defining the b g and r values of the midpoint pixel
        b = color[0]
        g = color[1]
        r = color[2]

        #Test equals the largest value (dominant value) out of the three values
        test = max(b, g, r)

        #if else statement to determine the image color and asssign it to the correct parameter
        if(test == b):
            self.color ="blue"
        elif(test == g):
            self.color = "green"
        elif(test == r):
            self.color = "red"

        return 0

#  def determineShape(self)
#
#  Summary of the determineShape Function:
#
#     The determineShape function
#
#  Parameters: self
#
#  Return Value: None
    def determineShape(self):
        gray =cv2.cvtColor(self.pic,cv2.COLOR_BGR2GRAY)
        #https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
        et, thresh_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        _, contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        i = 0
        for ct in contours:
            #skips the first contour as the first contour is the contour of the entire image
            if i == 0:
                i = 1
                continue
            #https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#ga0012a5fdaea70b8a9970165d98722b4c
            #passes in the countour, approximation accuracy of the arc length , and in this case true because everything is a closed curve
            corners = cv2.approxPolyDP(ct,0.01*cv2.arcLength(ct,True),True)
            #finds the center of the contour
            m = cv2.moments(ct)
            #pass coordinates to colors
            if m['m00'] != 0.0:
                x = int(m['m10']/m['m00'])
                y = int(m['m01']/m['m00'])
                self.determineColor(x,y)
            #if statements that determine the shape based upon the amount of contours
            if len(corners)==1:
                self.shape = "line"
            elif len(corners)==3:
                self.shape = "triangle"
            elif len(corners)==4:
                #https://docs.opencv.org/4.0.1/d3/dc0/group__imgproc__shape.html#ga2c759ed9f497d4a618048a2f56dc97f1
                #returns the top left coordinates as well as the width and height
                x,y,w,h = cv2.boundingRect(ct)
                #if the ratio of width and height is outside the specified parameters then its a square
                #ideally the ratio would be 1 but to us, something that appears to be a square may not be perfect to the computer
                if w/h >= 1.15 and w/h <=0.9:
                    self.shape = "rectangle"
                else:
                    self.shape = "square"
            elif len(corners)==5:
                self.shape="pentagon"
            elif len(corners)==6:
                self.shape = "hexagon"
            elif len(corners)==7:
                self.shape = "heptagon"
            elif len(corners)==8:
                self.shape = "octagon"
            else:
                self.shape="circle"
            #add a tuple with the x coordinate, the color, and the shape
            self.coordCorn.append(tuple([x,self.shape,self.color]))

            i+=1
        #sort the list of tuples by the x value. The lowest x value indicates the
        #image is the farthest to the left, and thus the first in the pattern
        self.coordCorn = sorted(self.coordCorn)


#  def parsePattern(self)
#
#  Summary of the parsePattern Function:
#
#     The parsePattern function iterates through self.coordCorn and compares the entery to the approved
#       list of entries included in self.validPatterns. If the pattern matches one in the list, it will
#       return a 1, otherwise will return a 0
#
#  Parameters: None
#
#  Return Value: None
    def parsePattern(self):
        #add the pattern to a string
        for i in range(len(self.coordCorn)):
            self.pattern+=self.coordCorn[i][1] + self.coordCorn[i][2]
        #check if the pattern is valid
        for i in self.validPatterns:
            if i == self.pattern:
                return 1
        return 0


#  def printPattern()
#
#  Summary of the print function:
#
#     The print function prints the pattern in the order in which it was recieved
#
#  Parameters: self
#
#  Return Value: None, but prints the pattern
    def printPattern(self):
        #format the stuff for a print statement
        store = ""
        for i in range(len(self.coordCorn)):
            store+="(" + self.coordCorn[i][2] + ","  + self.coordCorn[i][1] + ") "
        print(store)

# def printValidPatterns()
#
#   Summary of the printValidPatterns function:
#       The printValidPatterns functions prints the valid patterns for the user
#
#   Parameters: self
#
#   Return Value: None, but prints the valid patterns
    def printValidPatterns(self):
        print("Pattern 1: (Blue Circle), (Green Square), (Red Triangle)")
        print("Pattern 2: (Green Triangle), (Red Square), (Red Circle)")
        print("Pattern 3: (Blue Hexagon), (Blue Octagon), (Blue Heptagon)")
        print("Pattern 4: (Red Octagon), (Green Triangle), (Blue Ocatagon")
        print("Pattern 5: (Green Circle), (Blue Square), (Blue Octagon), (Red Heptagon), (Red Triangle), (Green Square)")
        print("Pattern 6: (Blue Circle), (Red Hexagon), (Green Heptagon), (Red Hexagon)\n")
