####
## This module is use to harvest all browser information such as,
## 	cache, history, cookies etc...
####


import shutil, glob, os, sys, time, json, loggin

## Purpose: Grab all known linux browser data based on file paths
## Glob: solves issue with regex and files paths with spaces
def linux_grab(dest):
	#Firefox
	for i in glob.glob('/home/*/.mozilla/firefox/*.default/Cache'):
			shutil.copy(i,dest + "/NIXFF1")

	for i in glob.glob('/root/.mozilla/firefox/*.default/Cache'):
			shutil.copy(i,dest + "/NIXFF2")

	#Chrome
	for i in glob.glob('/home/*/.config/google-chrome/Default/Application Cache/Cache/'):
			shutil.copy(i,dest + "/NIXCR1")

	for i in glob.glob('/home/*/.config/chromium/Default/Application Cache/Cache/'):
			shutil.copy(i,dest + "/NIXCR2")

	for i in glob.glob('/root/.config/chromium/Default/Application Cache/Cache/'):
			shutil.copy(i,dest+ "/NIXCR3")

	for i in glob.glob('/root/.config/google-chrome/Default/Application Cache/Cache/'):
			shutil.copy(i,dest + "/NIXCR4")

## Purpose: Grab all known windows browser data based on file paths
## Glob: solves issue with regex and files paths with spaces
def windows_grab(version, dest):
	if(version == "XP")
		
		#IE
		for i in glob.glob('C:\Documents and Settings\*\Local Settings\Temporary Internet Files\Content.IE5'):
			shutil.copy(i,dest + "\XPIE1")

		#Firefox
		for i in glob.glob('C:\Documents and Settings\*\Local Settings\Application Data\Mozilla\Firefox\Profiles\*.default\Cache'):
			shutil.copy(i,dest +"\XPFF1")
		
		#Chrome
		for i in glob.glob('C:\Documents and Settings\*\Local Settings\Application Data\Google\Chrome\User Data\Default\Cache'):
			shutil.copy(i,dest + "\XPCR1")

 
	if(version == "Vista")
		#IE
		for i in glob.glob('C:\Users\*\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5'):
			shutil.copy(i,dest + "\VIE1")

		for i in glob.glob('C:\Users\*\AppData\Local\Microsoft\Windows\Temporary Internet Files\Low\Content.IE5'):
			shutil.copy(i,dest + "\VIE2")

	if(version == "7")
		#IE
		for i in glob.glob('C:\Users\*\AppData\Local\Microsoft\Windows\Temporary Internet Files\Content.IE5'):
			shutil.copy(i,dest + "\Win7IE1")

		for i in glob.glob('C:\Users\*\AppData\Local\Microsoft\Windows\Temporary Internet Files\Low\Content.IE5'):
			shutil.copy(i,dest + "\Win7IE2")

		#Firefox
		for i in glob.glob('C:\Users\*\AppData\Local\Mozilla\Firefox\Profiles\*.default\Cache'):
			shutil.copy(i,dest + "\Win7FF1")

		#Chrome
		for i in glob.glob('C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\Cache'):
			shutil.copy(i,dest + "\Win7CR1")

	if(version == ("8" || "8.1"))
		#General Cache
		for i in glob.glob('C:\Users\*\AppData\Local\Microsoft\Windows\INetCache'):
			shutil.copy(i,dest + "\Win8Gen1")

		#IE
		for i in glob.glob('C:\Users\*\AppData\Local\Microsoft\Windows\History'):
			shutil.copy(i,dest + "\Win8IE1")

		#Firefox
		for i in glob.glob('C:\Users\*\AppData\Local\Mozilla\Firefox\Profiles\*.default\Cache'):
			shutil.copy(i,dest + "\Win8FF1")

		#Chrome
		for i in glob.glob('C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\Cache'):
			shutil.copy(i,dest + + "\Win8CR1")

## Purpose: Grab all known OSX browser data based on file paths
## Glob: solves issue with regex and files paths with spaces
def osx_grab(dest):
	#Firefox
	for i in glob.glob('/Users/*/Library/Caches/Firefox/Profiles/*.default/Cache'):
			shutil.copy(i,dest + "/OSXFF1")

	#Chrome
	for i in glob.glob('/Users/*/Caches/Google/Chrome/Default/Cache'):
			shutil.copy(i,dest + "/OSXCR1")


## Method Name: 
## Purpose: Initializes the logger for this BitCollector module.  
##  
def initializeLogger(self):  
	## Initialize the logger for this BitCollector module.  
        self.logger = logging.getLogger(self.__class__.__name__)  

        ## Override the logging level from the root logger. (Optional)  
        ## This is meant to give access to debug-level logging without  
        ## needing to see the debug output form the framework.  

        ## Set the logging level for the root logger. (Can be overridden for each module.)      
        if (self.logging_level.upper() == "DEBUG"):  
		self.logger.setLevel(logging.DEBUG)  

        elif (self.logging_level.upper() == "INFO"):  
            	self.logger.setLevel(logging.INFO)  

        elif (self.logging_level.upper() == "WARNING"):  
            	self.logger.setLevel(logging.WARNING)  

        elif (self.logging_level.upper() == "ERROR"):  
                self.logger.setLevel(logging.ERROR)  

        elif (self.logging_level.upper() == "CRITICAL"):  
                self.logger.setLevel(logging.CRITICAL)  

        else:  
            	print "Startup - bitCollector_main.RuntimeSettings.initializeRootLogger - WARNING - Unknown logging level \"" + self.logging_level + "\" Defaulting to DEBUG."  

            	self.logger.setLevel(logging.DEBUG)  

        self.logger.debug("Successfully started Browser logger!")



## Class Name: ModuleSettings  
##  
## Purpose: Hold information about the settings required to run this BitCollector module.  
class ModuleSettings():  
    	## Method Name: __init__  
    	##  
    	## Purpose: Initialize the settings required to start the framework.  
    	##  
    	## Parameters  
    	## 1. module - The name and parameters to pass to the BitCollector module to be initialized.  

    	def __init__(self, module):  
        	## Loop through the dictionary containing this module's name and settings.  
        	for key in module:  
            		## Grab the name of this module as known by bitCollector_main  
            		if (key == "name"):  
                		self.name = module[key]

            		## Grab the dictionary containing the list of settings dictionaries (head spinning yet? Mine was)
            		elif (key == "parameters"):  
                		## Loop through the list of dictionaries containing setting names and values.  
                		for param_pair in module[key]:  
                    			## Finally loop through each dictionary containing a single setting's name and value.  
                    			for param, value in param_pair.iteritems():  
                        			## Use an if-elif block to extract the settings and store them in named veriables.  
                        			if (param == "harvest_browser"):  
                            				self.destination = value 
                        			elif (param == "logging_level"):  
                            				self.logging_level = value  
                        			else:  
                            				print "Startup - Test1.RuntimeSettings.__init__ - ERROR - Unexpected parameter: " + str(param) + ". Ignoring."  

        	## Call the method to initialize the module-level logger.  
        	self.initializeLogger()  



## Method Name: main (Required)  
##  
## Purpose: Serves as the entry point into the script.  
##  
## Parameters (All Required)   
## 1. runtime_settings - An instance of the RuntimeSettings class containing settings required to start the framework.  
## 2. platform_details - An instance of the Platform class containing the platform-independent attributes as well as a platform-dependent object.  
## 3. module_dict      - The name and parameters to pass to the BitCollector module to be initialized as a dictionary.  
def main(framework_settings, platform_details, module_dict):
	import bitCollector_main

    	# Get a logger
    	main_logger = logging.getLogger("module_root")

    	## Initialize an instance of the ModuleSettings class to store the settings required to start the module.
    	module_settings = ModuleSettings(module_dict)

	if (framework_settings.harvest_browser):
		self.logger.debug("Somebody flipped the harvest_browser swtich")

    	# Check for OS type
	if(self.os_type == "mac"):
		OSX_grab("destination file path")

	elif(self.os_type == "nix"):
		linux_grab("destination file path")

	else:
		windows_grab(self.platform_details.version, "destination file path")
 

    	return 0
