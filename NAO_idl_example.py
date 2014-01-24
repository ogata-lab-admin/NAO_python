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
import ssr, ssr__POA
from naoqi import *

import traceback,threading

threads = []
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

    def connect(self, addr, port):
        self.proxy = ALProxy("ALMotion", addr, port)

    # void setAngles(in StringArray name, in FloatArray value, in float fractionSpeed)
    def setAngles(self, name, value, fractionSpeed):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.setAngles(name.data, value.data, fractionSpeed)
        except:
            traceback.print_exc()


    # FloatArray getAngles(in StringArray name, in boolean useSensors)
    def getAngles(self, name, useSensors):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        # print 'getAngles', name, ',', useSensors
        try:
            d = self.proxy.getAngles(name.data, useSensors)
            print '==>', d
            return ssr.FloatArray(d)
        except:
            traceback.print_exc()
            return ssr.FloatArray([])

    # void openHand(in string name)
    def openHand(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        self.proxy.openHand(name)

    # void closeHand(in string name)
    def closeHand(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        self.proxy.closeHand(name)

    # void setStiffness(in StringArray name, in FloatArray stiffnesses)
    def setStiffness(self, name, stiffnesses):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.setStiffnesses(name.data, stiffnesses.data)
        except:
            traceback.print_exc()

    # FloatArray getStiffness(in StringArray name)
    def getStiffness(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            d = self.proxy.getStiffnesses(name.data)
            return ssr.FloatArray(d)
        except:
            traceback.print_exc()
            return ssr.FloatArray([])

    # void rest()
    def rest(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.rest()
        except:
            traceback.print_exc()

    # void wakeUp()
    def wakeUp(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.wakeUp()
        except:
            traceback.print_exc()


    # void moveTo(in float x, in float y, in float theta)
    def moveTo(self, x, y, theta):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.moveTo(x, y, theta)
        except:
            traceback.print_exc()


    # void moveToward(in float vx, in float vy, in float vtheta)
    def moveToward(self, vx, vy, vtheta):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.moveToward(vx, vy, vtheta)
        except:
            traceback.print_exc()


    # FloatArray getRobotPosition()
    def getRobotPosition(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getRobotPosition()
        except:
            traceback.print_exc()


    # FloatArray getRobotVelocity()
    def getRobotVelocity(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getRobotVelocity()
        except:
            traceback.print_exc()


    # void stopMove()
    def stopMove(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.stopMove()
        except:
            traceback.print_exc()


    # boolean moveIsActive()
    def moveIsActive(self):
        #raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.moveIsActive()
        except:
            traceback.print_exc()


    # void waitUntilMoveIsFinished()
    def waitUntilMoveIsFinished(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.waitUntilMoveIsFinished()
        except:
            traceback.print_exc()


    # void moveInit()
    def moveInit(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.moveInit()
        except:
            traceback.print_exc()


    # void setWalkArmEnabled(in boolean leftArmEnable, in boolean rightArmEnable)
    def setWalkArmEnabled(self, leftArmEnable, rightArmEnable):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # BoolArray getWalkArmEnabled()
    def getWalkArmEnabled(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # FloatArray getPosition(in string name, in long space, in boolean useSensors)
    def getPosition(self, name, space, useSensors):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # void setPosition(in string name, in long space, in FloatArray position, in float fractionMaxSpeed, in long axisMask)
    def setPosition(self, name, space, position, fractionMaxSpeed, axisMask):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # void setTransform(in string name, in long space, in FloatArray transform, in float fractionMaxSpeed, in long axisMask)
    def setTransform(self, name, space, transform, fractionMaxSpeed, axisMask):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None

    # FloatArray getTransform(in string name, in long space, in boolean useSensorValues)
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
    def connect(self, addr, port):
        self.proxy = ALProxy("ALTextToSpeech", addr, port)

    # void say(in string stringToSay)
    def say(self, stringToSay):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            # print 'say ', stringToSay
            self.proxy.say(stringToSay)
        except:
            traceback.print_exc()

    # void setVolume(in float volume)
    def setVolume(self, volume):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        self.proxy.setVolume(volume)

    # float getVolume()
    def getVolume(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        return self.proxy.getVolume()

    # void setLanguage(in string language)
    def setLanguage(self, language):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        self.proxy.setLanguage(language)

    # string getLanguage()
    def getLanguage(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        return self.proxy.getLanguage()

    # StringArray getAvailableLanguages()
    def getAvailableLanguages(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        return self.proxy.getAvailableLanguages()


class ALBehaviorManager_i (ssr__POA.ALBehaviorManager):
    """
    @class ALBehaviorManager_i
    Example class implementing IDL interface ssr.ALBehaviorManager
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    def connect(self, addr, port):
        self.proxy = ALProxy("ALBehaviorManager", addr, port)
        pass

    # StringArray getInstalledBehaviors()
    def getInstalledBehaviors(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        return ssr.StringArray(self.proxy.getInstalledBehaviors())

    # StringArray getRunningBehaviors()
    def getRunningBehaviors(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        d = self.proxy.getRunningBehaviors()
        return ssr.StringArray(d)


    # boolean isBehaviorInstalled(in string name)
    def isBehaviorInstalled(self, name):
        #raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        return self.proxy.isBehaviorInstalled(name)

    # boolean isBehaviorRunning(in string name)
    def isBehaviorRunning(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        return self.proxy.isBehaviorRunning(name)

    # void runBehavior(in string name)
    def runBehavior(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.runBehavior(name)
        except:
            traceback.print_exc()


    # void stopAllBehaviors()
    def stopAllBehaviors(self):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        self.proxy.stopAllBehaviors()

    # void stopBehavior(in string name)
    def stopBehavior(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        self.proxy.stopBehavior(name)



class ALMemory_i (ssr__POA.ALMemory):
    """
    @class ALMemory_i
    Example class implementing IDL interface ssr.ALMemory
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    def connect(self, addr, port):
        self.proxy = ALProxy("ALMemory", addr, port)

    # void insertLongData(in string name, in long value)
    def insertLongData(self, name, value):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.insertLongData(name, value)
        except:
            traceback.print_exc()
        return None

    # void insertFloatData(in string name, in long value)
    def insertFloatData(self, name, value):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.insertFloatData(name, value)
        except:
            traceback.print_exc()
        return None

    # void insertStringData(in string name, in string value)
    def insertStringData(self, name, value):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.insertStringData(name, value)
        except:
            traceback.print_exc()
        return None


    # void insertLongArrayData(in string name, in LongArray value)
    def insertLongArrayData(self, name, value):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.insertLongArrayData(name, value.data)
        except:
            traceback.print_exc()
        return None


    # void insertFloatArrayData(in string name, in FloatArray value)
    def insertFloatArrayData(self, name, value):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.insertFloatArrayData(name, value.data)
        except:
            traceback.print_exc()
        return None

    # void insertStringArrayData(in string name, in StringArray value)
    def insertStringArrayData(self, name, value):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.insertStringArrayData(name, value.data)
        except:
            traceback.print_exc()
        return None


    # long getLongData(in string name)
    def getLongData(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getLongData(name)
        except:
            traceback.print_exc()
        return None

    # float getFloatData(in string name)
    def getFloatData(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getFloatData(name)
        except:
            traceback.print_exc()
        return None

    # string getStringData(in string name)
    def getStringData(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getStringData(name)
        except:
            traceback.print_exc()
        return None


    # LongArray getLongArrayData(in string name)
    def getLongArrayData(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getLongArrayData(name)
        except:
            traceback.print_exc()
        return None


    # FloatArray getFloatArrayData(in string name)
    def getFloatArrayData(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getFloatArrayData(name)
        except:
            traceback.print_exc()
        return None


    # StringArray getStringArrayData(in string name)
    def getStringArrayData(self, name):
        # raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result
        try:
            return self.proxy.getStringArrayData(name)
        except:
            traceback.print_exc()
        return None


class ALVideoDevice_i (ssr__POA.ALVideoDevice):
    """
    @class ALVideoDevice_i
    Example class implementing IDL interface ssr.ALVideoDevice
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    def connect(self, addr, port):
        self.proxy = ALProxy("ALVideoDevice", addr, port)

    # long getCameraModel(in long index)
    def getCameraModel(self, index):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # long getFrameRate(in long index)
    def getFrameRate(self, index):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # long getResolution(in long index)
    def getResolution(self, index):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # long getColorSpace(in long index)
    def getColorSpace(self, index):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # boolean setCameraParameter(in long id, in long value)
    def setCameraParameter(self, id, value):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # long getCameraParameter(in long id)
    def getCameraParameter(self, id):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # boolean setCameraParameterToDefault(in long id)
    def setCameraParameterToDefault(self, id):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result



class ALLeds_i (ssr__POA.ALLeds):
    """
    @class ALLeds_i
    Example class implementing IDL interface ssr.ALLeds
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    def connect(self, addr, port):
        self.proxy = ALProxy("ALLeds", addr, port)

    # void fade(in string name, in float intensity, in float duration)
    def fade(self, name, intensity, duration):
        #raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.fade(name, intensity, duration)
        except:
            traceback.print_exc()

    # void fadeRGB(in string name, in long rgb, in float duration)
    def fadeRGB(self, name, rgb, duration):
        #raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: None
        try:
            self.proxy.fadeRGB(name, rgb, duration)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = ALMotion_i()
    servant = ALLeds_i()

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

