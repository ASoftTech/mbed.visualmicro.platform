/* 
	Editor: http://www.visualmicro.com
	        visual micro and the arduino ide ignore this code during compilation. this code is automatically maintained by visualmicro, manual changes to this file will be overwritten
	        the contents of the Visual Micro sketch sub folder can be deleted prior to publishing a project
	        all non-arduino files created by visual micro and all visual studio project or solution files can be freely deleted and are not required to compile a sketch (do not delete your own code!).
	        note: debugger breakpoints are stored in '.sln' or '.asln' files, knowledge of last uploaded breakpoints is stored in the upload.vmps.xml file. Both files are required to continue a previous debug session without needing to compile and upload again
	
	Hardware: LPC1768, Platform=arm, Package=arm-supported
*/

#ifndef _VSARDUINO_H_
#define _VSARDUINO_H_
#define ARDUINO 166
#define ARDUINO_MAIN
#define __ARM__
#define __arm__
#define __cplusplus 201103L
#define ARDUINO_ARCH_ARM
#define ARDUINO_ARM_ARM_SUPPORTED_ARM_SUPPORTED_ARM_MBED_OS_SUPP_LPC1768

#include <wprogram.h>
#undef cli
#define cli()
#include "BlinkyTest1.ino"
#endif
