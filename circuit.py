#-----------------------------------------------------------------------
# File : circuit.py
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
# Description: This file contains the code to light up an LED green if the pattern is valid
#                  red if the pattern is invalid
#-----------------------------------------------------------------------
import RPi.GPIO as GPIO
import time

#  def LED(x)
#
#  Summary of the determineColor Function:
#
#     The LED function lights up a green or red led depending on if the
#       the pattern is valid. It gives text prompts if the gpio is not
#       if the gpio is not equipped
#
#  Parameters: x passes in a value of 0 or 1 to determine the validity of the pattern
#
#  Return Value: No return but lights the LED and prints out a statement
def LED(x):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    if(x == 1):
        #specifies which pin to use as an output
        GPIO.setup(18,GPIO.OUT) #Board pin 24

        #print statement to let user without the circuit board know the pattern was correct
        print("Pattern is correct! Turning on Green LED")

        #series of turning the LED on and off to create a flashing indication
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
    if(x == 0):
        #specifies which pin to use as an output
        GPIO.setup(16,GPIO.OUT) #Board pin 23

        #print statement to let user without the circuit board know the pattern was correct
        print("Pattern is incorrect! Turning on Red LED")

        #series of turning the LED on and off to create a flashing indication
        GPIO.output(16,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(16,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(16,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(16,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(16,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(16,GPIO.LOW)

    #ends the function with a cleanup and returns 0
    GPIO.cleanup()
    return 0
