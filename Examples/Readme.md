# Readme

## Overview

After cloning this repo you may need to run the following within the project directory to setup the needed libraries
```
mbed deploy
```

To Setup you need to set the target / toolchain and toolchain path
```
mbed config target LPC1768
mbed toolchain GCC_ARM
mbed config GCC_ARM_PATH "C:\Program Files (x86)\GNU Tools ARM Embedded\5.4 2016q3\bin"
```

To compile
```
mbed compile
```