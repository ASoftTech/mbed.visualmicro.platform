# Setup

## Overview

This is a list of steps to follow to get visual micro working with mbed <br>
Associated forum thread

  * http://www.visualmicro.com/forums/YaBB.pl?num=1478473145/0#5

## Installing the Mbed CLI

The first stage is to install all the tools you need for the mbed cli tool.
the mbed cli tool is a command line tool that can be used to create / manage / build mbed projects

  * Install the latest python 2.x version and make sure python is in your path - https://www.python.org/downloads/
  * Install the latest git and make sure git is in your path - https://git-scm.com/download/win
  * Install the latest mercurial and make sure the hg command is in your path - https://www.mercurial-scm.org/downloads <br>
    (some mbed libs use Mercurial)
  * Install gcc for arm, towards the end of the install make sure to select to add the tools to the path via the tick box - https://launchpad.net/gcc-arm-embedded
  * Finally install the python script mbed-cli via "pip install mbed-cli"

For more details I've put some information on a blog post here

  * http://grbd.github.io/posts/2016/11/06/using-the-mbed-cli/

## Visual Studio Setup

Next we need to make sure some options are enabled within Visual Studio <br>
Open up the Control Panel -> Program and Features -> Microsoft Visual Studio 2015, Right click Change

Make sure the following is ticked

  * The option for **Common Tools for Visual C++ 2015** should be enabled for C++ development
  * The option for **Visual C++ Mobile Development -> Visual C++ Android Development**
    to enable the Microsoft MI Debugger for GDB Debugging


## Visual Micro Setup

### Download the Micro Platforms Directory

Next we need to download the directory of "Micro Platforms" from this git repository. <br>
You can use git clone to do this

This directory needs to be located wherever you are storing the custom configs for Visual Micro.
By default the directory is

  * Windows 7 and above - "Documents\Visual Micro"
  * Windows XP -  "My Documents\Visual Micro"

so the full path should be something like "My Documents\Visual Micro\Micro Platforms"

The base directory can be changed within Visual Studio Settings under<br>
Tools -> Options -> Visual Micro -> General -> My Visual Micro Configs

Usually I set my setting to something like C:\Apps\VMicro\<br>
so that the full directory path ends up being C:\Apps\VMicro\Micro Platforms\

Ideally once complete we could do with ether adding in a platform.txt file for downloading the platform / boards <br>
or have this added into Visual Micro directly

### Configure the new Platform

Next we need to configure the new platform, to get Visual Studio to pick up the changes if it's already been started use <br>
Tools -> Visual Micro -> Reload Toolchains

Next Select
Tools -> Visual Micro -> Configure Ide Locations

In the drop down box on the left, select "Mbed OS 5.2"<br>
In the ide folder location this needs to be something like "C:\Apps\VMicro\Micro Platforms\mbed_os_52" <br>
This is assuming you've changed the config setting to use configs from C:\Apps\VMicro<br>
Next Click Okay

We should now be ready to create and build a new project
