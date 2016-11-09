# Todo

## GDB Debugging

Assuming everying has been installed that's needed under Visual Studio <br>
we should be able to get a menu entry to show up under <br>
vMicro -> Debugger -> Use Visual Studio Debugger

  * http://www.visualmicro.com/category/Arduino-Debug.aspx


## Arduino Due GDB

Visual Micro doesn't currently have the setup enabled for GDB debugging on the Arduino Due <br>
But I may be able to setup my own scripts for debugging via Visual Micro's openocd <br>
Currently the Arduino/Genuino Zero target has GDB enabled I can use as an example

See Links

  * http://www.visualmicro.com/forums/YaBB.pl?num=1477546499/0#6
  * http://www.visualmicro.com/forums/YaBB.pl?num=1478473145/0#5
  * http://www.visualmicro.com/post/2016/01/17/3rd-Party-Hardware-GDB-Configuration-Guide.aspx


## Mbed GDB

Based on a forum post I need something like 

**board.txt**
```
build.openocdscript=board/[mbed openOCD cfg name].cfg
```

**platform.txt**
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


## Build Debug options

To get more details we can enable

  * vMicro -> Compiler -> Verbose
  * vMicro -> Compiler -> Show Build Properties
