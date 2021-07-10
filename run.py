#-----------------------------------------------------------------------
# File : main.py
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
# Description: This program implemnts the functions found in the ShapeClass.py file as well as the circuit.py file.
#
#-----------------------------------------------------------------------
import shapeClass as shapes
import circuit

#  def run()
#
#  Summary of the run Function:
#
#     The run function implements many of the methods defined in the ShapeClass file. The function prints out information about using
#       program and then prompts the user to input one of the listed patterns. If the user enters the incorrect pattern, the program will
#       tell them and loop back to the main menu. The user can also quit the program by hitting the 'q' key. The selected pattern is then
#       passed into the class functions which will determine the shapes, color, and their order within the pattern. A 1 or a 0 is then passed to
#       the circuit.LED function which will either light a green LED or a RED LED if true or false.
#
#  Parameters: None
#
#  Return Value: None
def run():
    imageList = []
    temp = ""
    pattern = 0
    print("Welcome to the Pattern Machine. Please ensure the circuit board is properly connected to the computer\n")
    i = 0
    while True:
        print("Image choices: Pattern_1, Pattern_2, Pattern_3, Pattern_4")
        print("Pattern_5, Pattern_6, Pattern_7, Pattern_8, Pattern_9, Pattern_10\n")
        print("Please input image in correct formate of Pattern_#.png\n")
        temp = input("Please input an image, p for valid patterns, or enter q to quit: ")
        if temp =="q":
            break
        imageList.append(shapes.shapeClass())
        if temp == "p":
            imageList[i].printValidPatterns()
            i+=1
            continue
        if imageList[i].load_shape(temp)==False:
            print("Invalid choice, please choose a correct file")
            continue
        imageList[i].determineShape()
        pattern = imageList[i].parsePattern()
        print("The pattern you chose is: ",end=" ")
        imageList[i].printPattern()
        print("")
        circuit.LED(pattern)
        i+=1
