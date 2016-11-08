# Mbed Todo

## GDB Debugging

I need to look into the config for debugging with GDB
Based on the forum post

board.txt
```
build.openocdscript=board/[mbed openOCD cfg name].cfg
```

platform.txt
```
debug.tool=gdb
tools.gdb.pre_init.tool=openocd
tools.gdb.cmd=arm­none­eabi­gdb.exe
tools.gdb.path={runtime.tools.arm­none­eabi­gcc.path}/bin
tools.gdb.pattern="{path}/{cmd}" ­interpreter=mi ­d "{build.project_path}"
tools.gdb.openocd.cmd=bin/openocd.exe
tools.gdb.tcp=localhost:3333
tools.gdb.openocd.path={runtime.vm.ide.platforms.path}/default/tools/openocd­0.9.0
tools.gdb.openocd.params.verbose=­d2
tools.gdb.openocd.params.quiet=­d0
tools.gdb.openocd.pattern="{path}/{cmd}" ­-f "{path}\scripts\interface\stlink-v2.cfg" s "{path}/scripts/" ­f "{path}/scripts/{build.openocdscript}"
```

Visual Micro installs a copy of openocd under default\tools below where the applications2.txt resides

## Building

### Build Debug options

To get more details we can enable

  * vMicro -> Compiler -> Verbose
  * vMicro -> Compiler -> Show Build Properties

### Current Status

I can get the Mbed OS listed in the Visual Micro Platforms list, and the boards list for the items I've created. <br>
But trying to do a build leads to:

```
Board Properties
name=Mbed Generic
mcu=
runtime.ide.path=C:\Apps\VMicro\Micro Platforms\mbed_os_52
runtime.os=windows
build.system.path=C:\Apps\VMicro\Micro Platforms\mbed_os_52\hardware\arm\system
runtime.ide.version=166
target_package=arm
target_platform=arm
runtime.hardware.path=C:\Apps\VMicro\Micro Platforms\mbed_os_52\hardware
originalid=arm_arm_mbedos_generic
version=5.2.0
compiler.path=./
compiler.c.cmd=
compiler.c.flags=
compiler.c.elf.flags=
compiler.c.elf.cmd=mbed
compiler.S.flags=
compiler.cpp.cmd=mbed
compiler.cpp.flags=
compiler.cpp.elf.cmd=mbed
compiler.ar.cmd=msp430-ar
compiler.ar.flags=rcs
compiler.objcopy.cmd=
compiler.objcopy.eep.flags=
compiler.elf2hex.flags=
compiler.elf2hex.cmd=
compiler.ldflags=
compiler.size.cmd=
recipe.c.o.pattern=""
recipe.cpp.o.pattern=""
recipe.ar.pattern=""
recipe.c.combine.pattern="{compiler.path}{compiler.c.elf.cmd}" compile {build.mcu} -t GCC_ARM"
recipe.cpp.combine.pattern="{compiler.path}{compiler.cpp.elf.cmd}" compile {build.mcu} -t GCC_ARM"
recipe.objcopy.hex.pattern=""
recipe.size.pattern=""
vm.platform.root.path=C:\Apps\VMicro\Micro Platforms\mbed_os_52
runtime.vm.boardinfo.id=arm_arm_arm_mbedos_generic
runtime.vm.boardinfo.name=arm_arm_arm_mbedos_generic
runtime.vm.boardinfo.desc=Mbed Generic
runtime.vm.boardinfo.src_location=C:\Apps\VMicro\Micro Platforms\mbed_os_52\hardware\arm
ide.hint=Mbed OS 5.2
ide.default.platform=arm
ide.platformswithoutpackage=true
ide.location.preferences=%VM_APPDATA_ROAMING%\mbed_os_52\preferences.txt
ide.location.key=mbed_os_52
ide.location.ide.winreg=Mbed OS 5.2 Application
ide.location.sketchbook.winreg=Mbed OS 5.2 Sketchbook
ide.location.sketchbook.preferences=sketchbook.path
ide.location.sketchbook.default=%MYDOCUMENTS%\mbed_os_52
ide.board_folders_are_platform_names=false
ide.appid=mbed_os_52
ide.iscustomapp=1
location.sketchbook=C:\Users\richard\Documents\Arduino
build.architecture=Common7
vmresolved.compiler.path=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\
vmresolved.tools.path=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7
vm.core.include=wprogram.h
build.board=ARM_ARM_ARM_ARM_MBEDOS_GENERIC
vm.boardsource.path=C:\Apps\VMicro\Micro Platforms\mbed_os_52\hardware\arm
runtime.platform.path=C:\Apps\VMicro\Micro Platforms\mbed_os_52\hardware\arm
vm.platformname.name=arm
build.arch=ARM
builder.noino=false
vm.runtime.compiler.showwarnings=false
vm.runtime.upload.verbose=false
vm.runtime.upload.verify=false
vm.runtime.compiler.auto_discover_includes=true
build.vm.build.vmdebug=1
build.vm.build.isgdb=0
build.vm.build.optimised=1
vm.last.buildpath=C:\Users\richard\AppData\Local\Temp\VMicroBuilds\BlinkyTest1\arm_arm_arm_mbedos_generic

Compiling debug version of 'BlinkyTest1' for 'Mbed Generic'
Build folder: file:///C:/Users/richard/AppData/Local/Temp/VMicroBuilds/BlinkyTest1/arm_arm_arm_mbedos_generic
Additional Defines: VM_DEBUG;VM_DEBUG_ENABLE 1;VM_DEBUG_BANDWIDTH_THROTTLE_MS 50;VM_DEBUGGER_TYPE_HARDWARESERIAL 0;VM_DEBUGGER_TYPE_SOFTWARESERIAL 1;VM_DEBUGGER_TYPE_FASTSERIAL 2;VM_DEBUGGER_TYPE_USB 3;VM_DEBUGGER_TYPE_TEENSY 4;VM_DEBUGGER_TYPE_UART 5;VM_DEBUGGER_TYPE_USART 6;VM_DEBUGGER_TYPE_USBSERIAL 7;VM_DEBUGGER_TYPE_TTYUART 8;VM_DEBUGGER_TYPE_NET_CONSOLE 9;VM_DEBUGGER_TYPE_Uart 10;VM_DEBUGGER_TYPE_COSA 11;VM_DEBUGGER_TYPE_CDCSerialClass 12;VM_DEBUGGER_TYPE_HARDWARESERIAL1 13;VM_DEBUGGER_TYPE_HARDWARESERIAL2 14;VM_DEBUGGER_TYPE_HARDWARESERIAL3 15;VM_DEBUGGER_TYPE VM_DEBUGGER_TYPE_HARDWARESERIAL;VM_DEBUG_BREAKPAUSE;
Architecture Tools: ./
Sketchbook: file:\\\C:\Users\richard\Documents\Arduino
Sketch Include Paths
Core Include Paths
Include Path ''
Library Include Paths (1)
All import libraries will be re-compiled
System.ArgumentException: The path is not of a legal form.
   at System.IO.Path.LegacyNormalizePath(String path, Boolean fullCheck, Int32 maxPathLength, Boolean expandShortPaths)
   at System.IO.Path.NormalizePath(String path, Boolean fullCheck, Int32 maxPathLength, Boolean expandShortPaths)
   at System.IO.Path.GetFullPathInternal(String path)
   at System.IO.DirectoryInfo.Init(String path, Boolean checkHost)
   at System.IO.DirectoryInfo..ctor(String path)
   at Visual.Micro.MiroAppAPI.SketchCompiler.CreateFileTimeListXml(String fileType, String sPath, String outputPath)
   at Visual.Micro.MiroAppAPI.SketchCompilerArduino._compile(SketchBuilder lsketch, String primaryClassName, Boolean verbose, Boolean isDebug)
   at Visual.Micro.MiroAppAPI.SketchCompilerArduino.compile(SketchBuilder lsketch, String primaryClassName, Boolean verbose, Boolean isDebug)
   at Visual.Micro.Visual.Studio.Arduino.AddInApp._CompileDo(Project oProject, Boolean IsDebugStartCommand, Boolean isRebuild, Boolean UseGdbIfAvailable)
   at Visual.Micro.Visual.Studio.Arduino.AddInApp.CompileDo(Project oProject, Boolean IsDebugStartCommand, Boolean isRebuild, Boolean UseGdbIfAvailable)
   at Visual.Micro.Visual.Studio.Arduino.AddInApp.Compile(Project oProject, Boolean IsDebugStartCommand, Boolean IsRebuild, Boolean UseGdbIfAvailable)
```



