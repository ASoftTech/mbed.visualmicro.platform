# Creating a new Project for mbed with Visual Micro

## Overview

This is still a bit experimental at the moment, ideally this could do with being put into a project template in some way <br>
But for now I've just listed the steps needed to setup a new project

I've placed an example blinky project within the Examples directory of this repo

## Setting up a new project

First create a new Solution within Visual Studio <br>
Next add a new Visual Micro Project within the Solution <br>
This should create all the files needed for Visual Micro to operate etc

Next open up a command promt and change directory to the Project directory
```
cd VisualMicroProject
```

Use the mbed cli to add in any needed files
```
mbed new .
```

## Adding Sources

A basic example for main.cpp for blinky would be something like
```
#include "mbed.h"

DigitalOut led1(LED1);

// main() runs in its own thread in the OS
// (note the calls to Thread::wait below for delays)
int main() {
    while (true) {
        led1 = !led1;
        Thread::wait(500);
    }
}
```

To add this to the project within visual studio <br>
Select Project -> Show all files <br>
Right click the main.cpp and select "Include to Project" <br>
Select Project -> Show all files, to hide anything not needed again <br>

## Git ignore

You may need to define a .gitignore file to ignore some of the files that shouldn't be included into the git repository

.gitignore
```
# Local files to ignore
.build
.mbed
projectfiles
*.py*

# Downloaded libs to ignore
mbed-os/
```

The downloaded libraries ideally shouldn't be checked in <br>
this is because mbed can download these for other users automatically by using "mbed deploy" <br>
This reads in any .lib text files and uses them to auto download any needed libs and dependencies
