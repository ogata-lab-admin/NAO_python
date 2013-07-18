#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file NAO.py
 @brief NAO RT Component
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import NAO_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from NAO_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
nao_spec = ["implementation_id", "NAO", 
		 "type_name",         "NAO", 
		 "description",       "NAO RT Component", 
		 "version",           "1.0.0", 
		 "vendor",            "Ogata Lab Waseda Univ.", 
		 "category",          "Robot", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.ipaddress", "nao.local",
		 "conf.default.port", "9559",
		 "conf.default.debug", "1",
		 "conf.default.camera_id", "0",
		 "conf.default.num_channel", "1",
		 "conf.default.interleaved", "1",
		 "conf.default.num_samples", "16000",
		 "conf.default.channel_name", "fromt",
		 "conf.default.enable_camera", "0",
		 "conf.default.enable_audio", "0",
		 "conf.__widget__.ipaddress", "text",
		 "conf.__widget__.port", "text",
		 "conf.__widget__.debug", "text",
		 "conf.__widget__.camera_id", "radio",
		 "conf.__widget__.num_channel", "radio",
		 "conf.__widget__.interleaved", "radio",
		 "conf.__widget__.num_samples", "text",
		 "conf.__widget__.channel_name", "checkbox",
		 "conf.__widget__.enable_camera", "radio",
		 "conf.__widget__.enable_audio", "radio",
		 "conf.__constraints__.camera_id", "(0, 1)",
		 "conf.__constraints__.num_channel", "(1,2,4)",
		 "conf.__constraints__.interleaved", "(0, 1)",
		 "conf.__constraints__.channel_name", "(front, rear, left right)",
		 "conf.__constraints__.enable_camera", "(0, 1)",
		 "conf.__constraints__.enable_audio", "(0,1)",
		 ""]
# </rtc-template>

##
# @class NAO
# @brief NAO RT Component
# 
# 
class NAO(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		w = 640
		h = 480
		bpp = 24
		format = "bitmap"
		fDiv = 1.0
		pixels = []
		self._d_camera = RTC.CameraImage(RTC.Time(0,0), w, h, bpp, format, fDiv, pixels)
		"""
		"""
		self._cameraOut = OpenRTM_aist.OutPort("camera", self._d_camera)
		self._d_audio = RTC.TimedOctetSeq(RTC.Time(0,0),[])
		"""
		"""
		self._audioOut = OpenRTM_aist.OutPort("audio", self._d_audio)
		self._d_jointAngle = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._jointAngleOut = OpenRTM_aist.OutPort("jointAngle", self._d_jointAngle)
		self._d_bumper = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
		"""
		bumper data (lfoot_left, lfoot_right, rfoot_left, rfoot_right)
		"""
		self._bumperOut = OpenRTM_aist.OutPort("bumper", self._d_bumper)
		self._d_touch = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
		"""
		touch detection (head_back, head_center, head_front, rhand_back,
		rhand_center, rhand_front, lhand_back, lhand_center, lhand_front)
		"""
		self._touchOut = OpenRTM_aist.OutPort("touch", self._d_touch)
		self._d_sonar = RTC.TimedBooleanSeq(RTC.Time(0,0),[])
		"""
		sonar detection, (left, right)
		"""
		self._sonarOut = OpenRTM_aist.OutPort("sonar", self._d_sonar)

		"""
		"""
		self._NAO_srvPort = OpenRTM_aist.CorbaPort("NAO_srv")

		"""
		"""
		self._motion = ALMotion_i()
		"""
		"""
		self._textToSpeech = ALTextToSpeech_i()
		"""
		"""
		self._behaviorManager = ALBehaviorManager_i()
		"""
		"""
		self._memory = ALMemory_i()
		"""
		"""
		self._leds = ALLeds_i()
		"""
		"""
		self._videoDevice = ALVideoDevice_i()
		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  ipaddress
		 - DefaultValue: nao.local
		"""
		self._ipaddress = ['nao.local']
		"""
		
		 - Name:  port
		 - DefaultValue: 9559
		"""
		self._port = [9559]
		"""
		
		 - Name:  debug
		 - DefaultValue: 1
		"""
		self._debug = [1]
		"""
		
		 - Name:  camera_id
		 - DefaultValue: 0
		"""
		self._camera_id = [0]
		"""
		
		 - Name:  num_channel
		 - DefaultValue: 1
		"""
		self._num_channel = [1]
		"""
		
		 - Name:  interleaved
		 - DefaultValue: 1
		"""
		self._interleaved = [1]
		"""
		
		 - Name:  num_samples
		 - DefaultValue: 16000
		"""
		self._num_samples = [16000]
		"""
		
		 - Name:  channe_name
		 - DefaultValue: fromt
		"""
		self._channe_name = ['fromt']
		"""
		
		 - Name:  enable_camera
		 - DefaultValue: 0
		"""
		self._enable_camera = [0]
		"""
		
		 - Name:  enable_audio
		 - DefaultValue: 0
		"""
		self._enable_audio = [0]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("ipaddress", self._ipaddress, "nao.local")
		self.bindParameter("port", self._port, "9559")
		self.bindParameter("debug", self._debug, "1")
		self.bindParameter("camera_id", self._camera_id, "0")
		self.bindParameter("num_channel", self._num_channel, "1")
		self.bindParameter("interleaved", self._interleaved, "1")
		self.bindParameter("num_samples", self._num_samples, "16000")
		self.bindParameter("channel_name", self._channe_name, "fromt")
		self.bindParameter("enable_camera", self._enable_camera, "0")
		self.bindParameter("enable_audio", self._enable_audio, "0")
		
		# Set InPort buffers
		
		# Set OutPort buffers
		self.addOutPort("camera",self._cameraOut)
		self.addOutPort("audio",self._audioOut)
		self.addOutPort("jointAngle",self._jointAngleOut)
		self.addOutPort("bumper",self._bumperOut)
		self.addOutPort("touch",self._touchOut)
		self.addOutPort("sonar",self._sonarOut)
		
		# Set service provider to Ports
		self._NAO_srvPort.registerProvider("ALMotion", "ssr::ALMotion", self._motion)
		self._NAO_srvPort.registerProvider("ALTextToSpeech", "ssr::ALTextToSpeech", self._textToSpeech)
		self._NAO_srvPort.registerProvider("ALBehaviorManager", "ssr::ALBehaviorManager", self._behaviorManager)
		self._NAO_srvPort.registerProvider("ALMemory", "ssr::ALMemory", self._memory)
		self._NAO_srvPort.registerProvider("ALLeds", "ssr::ALLeds", self._leds)
		self._NAO_srvPort.registerProvider("ALVideoDevice", "ssr::ALVideoDevice", self._videoDevice)
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		self.addPort(self._NAO_srvPort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
		try :
			self._textToSpeech.connect(self._ipaddress[0], self._port[0])
			self._behaviorManager.connect(self._ipaddress[0], self._port[0])
		except Exception, e:
			print e
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
		
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def NAOInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=nao_spec)
    manager.registerFactory(profile,
                            NAO,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    NAOInit(manager)

    # Create a component
    comp = manager.createComponent("NAO")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()
