#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file NAO_idl_examplefile.py
 @brief Python example implementations generated from NAO.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import ssr, ssr__POAimport ssr, ssr__POA


class ALMotion_i (ssr__POA.ALMotion):
    """
    @class ALMotion_i
    Example class implementing IDL interface ssr.ALMotion
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # void setAngles(in StringArray name, in DoubleArray value, in double fractionSpeed)
    def setAngles(self, name, value, fractionSpeed):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # DoubleArray getAngles(in StringArray name, in bool useSensors)
    def getAngles(self, name, useSensors):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void openHane(in string name)
    def openHane(self, name):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void closeHand(in string name)
    def closeHand(self, name):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void setStiffness(in StringArray name, in DoubleArray stiffnesses)
    def setStiffness(self, name, stiffnesses):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # DoubleArray getStiffness(in StringARray name)
    def getStiffness(self, name):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void rest()
    def rest(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void wakeUp()
    def wakeUp(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void moveTo(in double x, in double y, in double theta)
    def moveTo(self, x, y, theta):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void moveToward(in double vx, in double vy, in double vtheta)
    def moveToward(self, vx, vy, vtheta):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # DoubleArray getRobotPosition()
    def getRobotPosition(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # DoubleArray getRobotVelocity()
    def getRobotVelocity(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void stopMove()
    def stopMove(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # bool moveIsActive()
    def moveIsActive(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void waitUntilMoveIsFinished()
    def waitUntilMoveIsFinished(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void moveInit()
    def moveInit(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void setWalkArmEnabled(in bool leftArmEnable, in bool rightArmEnable)
    def setWalkArmEnabled(self, leftArmEnable, rightArmEnable):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # BoolArray getWalkArmEnabled()
    def getWalkArmEnabled(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # DoubleArray getPosition(in string name, in int space, in bool useSensors)
    def getPosition(self, name, space, useSensors):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void setPosition(in string name, in int space, in DoubleArray position, in double fractionMaxSpeed, in int axisMask)
    def setPosition(self, name, space, position, fractionMaxSpeed, axisMask):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void setTransform(in string name, in int space, in DoubleArray transform, in double fractionMaxSpeed, in int axisMask)
    def setTransform(self, name, space, transform, fractionMaxSpeed, axisMask):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # DoubleArray getTransform(in string name, in int space, in bool useSensorValues)
    def getTransform(self, name, space, useSensorValues):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result



class ALTextToSpeech_i (ssr__POA.ALTextToSpeech):
    """
    @class ALTextToSpeech_i
    Example class implementing IDL interface ssr.ALTextToSpeech
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # void say(in string stringToSay)
    def say(self, stringToSay):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void setVolume(in double volume)
    def setVolume(self, volume):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # double getVolume()
    def getVolume(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void setLanguage(in string language)
    def setLanguage(self, language):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # string getLanguage()
    def getLanguage(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # StringArray getAvailableLanguages()
    def getAvailableLanguages(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = ALMotion_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

